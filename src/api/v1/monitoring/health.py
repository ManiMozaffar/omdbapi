from fastapi import APIRouter

from app.schemas.extras import Health
from core.config import config

router = APIRouter()


@router.get("/health")
async def health() -> Health:
    return Health(version=config.RELEASE_VERSION, status="Healthy")
