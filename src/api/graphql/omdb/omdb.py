from fastapi import APIRouter
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
import graphene

from app.controllers import OMDBController

router = APIRouter()
router.add_route(
    "/omdb",
    GraphQLApp(
        schema=graphene.Schema(query=OMDBController),
        on_get=make_graphiql_handler()
    )
)
