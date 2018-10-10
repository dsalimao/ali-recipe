from concurrent import futures
import time
import grpc
from proto.recipe_service_pb2 import GetRecipeRequest
from proto.recipe_service_pb2 import GetRecipeResponse
from proto.recipe_service_pb2 import CreateRecipeRequest
from proto.recipe_service_pb2 import CreateRecipeResponse
from proto.recipe_service_pb2 import Recipe
from proto import recipe_service_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class RecipeService(recipe_service_pb2_grpc.RecipeServiceServicer):
    """Provides methods that implement functionality of recipe server."""

    def __init__(self):
        # self.db = route_guide_resources.read_route_guide_database()
        pass

    def GetRecipe(self, request, context):
        recipe = Recipe()
        recipe.name = "rice"
        resp = GetRecipeResponse()
        resp.recipe = recipe
        return resp

    def CreateRecipe(self, request, context):
        resp = CreateRecipeResponse()
        return resp


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recipe_service_pb2_grpc.add_RecipeServiceServicer_to_server(
        RecipeService(), server)
    server.add_insecure_port('[::]:10025')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()