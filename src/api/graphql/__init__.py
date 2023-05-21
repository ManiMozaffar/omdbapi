from fastapi import APIRouter
from .omdb import router as graphql_router

router = APIRouter()
router.include_router(graphql_router)
