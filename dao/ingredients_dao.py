from dao.conn_pool import mysql_pool
from proto.recipe_service_pb2 import Ingredients


def _create_table():
    mysql_pool.execute('''
    CREATE TABLE ingredients(
    type VARCHAR(100) CHARACTER SET utf8mb4 NOT NULL PRIMARY KEY,
    calorie INT,
    price INT,
    url TEXT,
    weight INT,
    volume INT);
    ''')

def get_ingredients(type):
    """
    get ingredients from db
    :param type: IngredientsType
    :return Ingredients
    """
    type_str = Ingredients.IngredientsType.Name(type)

    row=mysql_pool.execute('''
    SELECT * FROM ingredients WHERE type = (%s)
    ''', (type_str,), return_one=True)

    if row==None:
        return None

    ing = Ingredients()
    ing.ingredients_type = Ingredients.IngredientsType.Value(row['type'])
    if row['calorie']:
        ing.calorie = row['calorie']
    if row['price']:
        ing.price = row['price']
    if row['url']:
        ing.picture_urls = row['url']
    if row['weight']:
        ing.kilogram = row['weight']
    if row['volume']:
        ing.milliliter = row['volume']

    return ing


def create_ingredients(ingredients):
    """
    create new ingredients
    """
    type_str = Ingredients.IngredientsType.Name(ingredients.ingredients_type)

    exist = get_ingredients(ingredients.ingredients_type)
    if exist != None:
        raise Exception("Ingredients {} already exists".format(type_str))

    mysql_pool.execute('''
    INSERT INTO ingredients(type, weight, calorie) VALUES (%s, %s, %s);
    ''', (type_str, ingredients.kilogram, ingredients.calorie))



if __name__=="__main__":
    get_ingredients(Ingredients.OIL)

    # rice = Ingredients()
    # rice.ingredients_type = Ingredients.RICE
    # rice.calorie = 200
    # rice.kilogram = 100
    # create_ingredients(rice)