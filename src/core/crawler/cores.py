from .abc import AbstractCore
import httpx


class HTTPXCore(AbstractCore):
    def __init__(self, **_):
        with httpx.Client() as client:
            self.headers = client.headers

    async def get(self, url, params) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url, params=params, headers=self.headers
            )
            return response

    async def post(self, url, params, body) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url, params=params, json=body, headers=self.headers
            )
            return response

    async def put(self, url, params, body) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.put(
                url, params=params, json=body, headers=self.headers
            )
            return response

    async def delete(self, url, params, body) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.delete(
                url, params=params, json=body, headers=self.headers
            )
            return response

    async def add_to_header(self, key, value) -> dict:
        self.headers[key] = value
