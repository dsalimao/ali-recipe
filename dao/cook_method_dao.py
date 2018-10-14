from dao.conn_pool import mysql_pool
from proto.recipe_service_pb2 import CookMethod


def _create_table():
    mysql_pool.execute('''
    CREATE TABLE cook_method(
    type VARCHAR(100) CHARACTER SET utf8mb4 NOT NULL PRIMARY KEY);
    ''')

def get_cook_method(type):
    """
    get cook method from db
    :param type: CookMethodType
    :return CookMethod
    """
    type_str = CookMethod.CookMethodType.Name(type)

    row=mysql_pool.execute('''
    SELECT * FROM cook_method WHERE type = (%s)
    ''', (type_str,), return_one=True)

    if row ==None:
        return None

    coo = CookMethod()
    coo.cook_method_type = CookMethod.CookMethodType.Value(row['type'])

    return coo


def create_cook_method(cook_method):
    """
    create new cook method
    """
    type_str = CookMethod.CookMethodType.Name(cook_method.cook_method_type)

    exist = get_cook_method(cook_method.cook_method_type)
    if exist != None:
        raise Exception("Cook method {} already exists".format(type_str))

    mysql_pool.execute('''
    INSERT INTO cook_method(type) VALUES (%s);
    ''', (type_str,))


if __name__=="__main__":
    print(get_cook_method(CookMethod.STEAM))
    steam = CookMethod()
    steam.cook_method_type = CookMethod.STEAM
    create_cook_method(steam)
    print(get_cook_method(CookMethod.STEAM))
