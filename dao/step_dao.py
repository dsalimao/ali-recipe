from dao.conn_pool import mysql_pool
from proto.recipe_service_pb2 import Step
from proto.recipe_service_pb2 import GetIngredients
from proto.recipe_service_pb2 import CookIt
from proto.recipe_service_pb2 import Ingredients
from proto.recipe_service_pb2 import CookMethod


def _create_table():
    mysql_pool.execute('''
    CREATE TABLE step(
    id VARCHAR(100) NOT NULL PRIMARY KEY,
    recipe_id VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL,
    ingredients_type VARCHAR(100),
    serving_count DOUBLE,
    cook_method_type VARCHAR(100),
    seconds INT,
    INDEX by_recipe_id (recipe_id)
    );
    ''')

    mysql_pool.execute('''
    CREATE TABLE prev_step(
    cur_id VARCHAR(100) NOT NULL,
    prev_id VARCHAR(100) NOT NULL,
    INDEX by_cur_id(cur_id)
    );
    ''')


def get_step(step_id):
    """
    get step by unique id
    :param step_id: string
    :return Step
    """
    row=mysql_pool.execute('''
    SELECT * FROM step WHERE id = (%s)
    ''', (step_id,), return_one=True)

    if row ==None:
        return None

    return _build_step(row)


def get_all_steps(recipe_id):
    """
    get all steps for a recipe
    :param recipe_id: string
    :return [Step]
    """
    rows = mysql_pool.execute('''
    SELECT * FROM step WHERE recipe_id = (%s)
    ''', (recipe_id,), return_one=False)

    steps = []

    for row in rows:
        steps.append(_build_step(row))

    return steps


def _build_step(row):
    """
    build Step proto from a mysql row
    """
    step = Step()
    step.id = row['id']
    step.previous_step_ids.extend(_get_prev_steps(step.id))
    step.recipe_id = row['recipe_id']
    step.type = Step.StepType.Value(row['type'])
    if step.type == Step.GET_INGREDIENTS:
        gi = GetIngredients()
        gi.ingredients_type = Ingredients.IngredientsType.Value(row['ingredients_type'])
        gi.serving_count = row['serving_count']
        step.get_ingredients = gi
    elif step.type == Step.COOK_IT:
        ci = CookIt()
        ci.cook_method_type = CookMethod.CookMethodType.Value(row['cook_method_type'])
        ci.seconds = row['seconds']
        step.cook_it = ci
    return step


def _get_prev_steps(step_id):
    rows = mysql_pool.execute('''
    SELECT * FROM prev_step WHERE cur_id = (%s)
    ''', (step_id,), return_one=False)

    prev_steps = []

    for row in rows:
        prev_steps.append(row['prev_id'])

    return prev_steps


def create_step_method(step):
    """
    create new recipe step
    """
    exist = get_step(step.id)
    if exist != None:
        raise Exception("Step {} already exists".format(step.id))

    if step.type == Step.COOK_IT:
        mysql_pool.execute('''
        INSERT INTO step(id, recipe_id, type, cook_method_type, seconds) VALUES (%s,%s,%s,%s,%s);
        ''', (step.id,step.recipe_id,CookMethod.CookMethodType.Name(step.cook_it.cook_method_type),
              step.cook_it.seconds))
    elif step.type == Step.GET_INGREDIENTS:
        mysql_pool.execute('''
        INSERT INTO step(id, recipe_id, type, ingredients_type, serving_count) VALUES (%s,%s,%s,%s,%s);
        ''', (step.id,step.recipe_id,Ingredients.IngredientsType.Name(step.get_ingredients.ingredients_type),
              step.get_ingredients.serving_count))

    for prev_step in step.previous_step_ids:
        mysql_pool.execute('''
        INSERT INTO prev_step(cur_id, prev_id) VALUES (%s,%s);
        ''', (step.id, prev_step))


if __name__=="__main__":
    pass
