# Cartesian product X×Y between two sets X and Y is the set of all possible ordered pairs with first element from X and second element from Y
#    X×Y={(x,y):x∈X and y∈Y}
import itertools
from enum import Enum

# # region: Product of elements in a list of lists
# mylist = [
#    [1, 2, 3],
#    ['a', 'b'],
#    [4, 5]
# ]
# for element in itertools.product(*mylist):
#     print(element)

# # endregion

# # region: Product of two lists
# arr1 = [1, 2, 3]
# arr2 = [5, 6, 7]
# print(list(itertools.product(arr1, arr2)))
# # endregion

# region: Two Enums

class TestCartesianProduct():
    class Environment(Enum):
        DEVELOPMENT = 'DEV'
        TESTING = 'TEST'
        PRODUCTION = 'PROD'

    class Database(Enum):
        POSTGRESQL = "POSTGRESQL"
        MYSQL = "MYSQL"
        MONGODB = "MONGODB"
        REDIS = "REDIS"

    # print(*list(itertools.product(Environment, Database)), sep="\n")
    # # x = list(itertools.product(Environment, Database))
    # # for y in x:
    # #     print(y[0], " - ", y[1])

    # unpack items to Environment, Database
    for database, environment in list(itertools.product(Database, Environment)):
        print(database, " - ", environment)

# endregion
