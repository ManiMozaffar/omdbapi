from fastapi import APIRouter

from .graphql import router as graphql_router
from .v1 import router as v1_router

router = APIRouter()
router.include_router(graphql_router, prefix="/graphql")
router.include_router(v1_router, prefix="/v1")
