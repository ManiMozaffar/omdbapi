import pytest
from httpx import AsyncClient
from tests.factory.query import create_fake_query


@pytest.mark.asyncio
async def test_omdb_fake_query(client: AsyncClient):
    client.headers.update({'Content-Type': 'application/json'})
    response = await client.post(
        "graphql/omdb",
        json={"query": create_fake_query()}
    )
    assert response.status_code == 200
    assert type(response.json()["data"]["movies"]["totalCount"]) == int


@pytest.mark.asyncio
async def test_omdb_limit_and_skip(client: AsyncClient):
    client.headers.update({'Content-Type': 'application/json'})
    first_response = await client.post(
        "graphql/omdb",
        json={"query": create_fake_query(default_name="Bad", limit=25, skip=0)}
    )
    second_response = await client.post(
        "graphql/omdb",
        json={"query": create_fake_query(default_name="Bad", limit=25, skip=5)}
    )
    assert (
        first_response.status_code == 200
    ) and (
        second_response.status_code == 200
    )

    assert first_response.json()["data"]["movies"]["totalCount"] > 25

    assert (
        first_response.json()["data"]["movies"]["edges"][0]["node"]["imdbID"]
    ) != (
        second_response.json()["data"]["movies"]["edges"][0]["node"]["imdbID"]
    )

    assert (
        len(first_response.json()["data"]["movies"]["edges"])
    ) == (
        len(second_response.json()["data"]["movies"]["edges"])
    ) == 25
