from proto.recipe_service_pb2 import Recipe
from proto.recipe_service_pb2 import Step
from proto.recipe_service_pb2 import GetIngredients
from proto.recipe_service_pb2 import CookIt
from proto.recipe_service_pb2 import Ingredients
from proto.recipe_service_pb2 import CookMethod
from graph.general_graph import GeneralGraph
from graph.general_graph import GraphNode


def to_general_graph(recipe):
    """
    build a graph from steps in a recipe
    :param recipe: Recipe
    :return GeneralGraph
    """
    steps = recipe.steps;
