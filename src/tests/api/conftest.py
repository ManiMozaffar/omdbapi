from typing import Any, Generator

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient

from core.server import create_app


@pytest.fixture(scope="session")
def app() -> Generator[FastAPI, Any, None]:
    """
    Create a new FastAPI app
    """
    app = create_app()
    yield app


@pytest_asyncio.fixture(scope="function")
async def client(app: FastAPI) -> AsyncClient:
    """
    Create a new FastAPI AsyncClient
    """
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
