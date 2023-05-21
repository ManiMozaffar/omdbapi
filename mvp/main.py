###############################################################################
#                                 MVP Playground                              #
###############################################################################
# Author: Mani
# Date: May 21, 2023
# Description: This code represents an MVP (Minimum Viable Product) playground
#              for experimentation and learning purposes. It does not adhere to
#              proper architecture design and coding practices.

# Note: The implementation of graphene in this code could be improved by using
#       pydantic models for better data validation and structure. Additionally,
#       considering the use of an is_null property instead of a Nullable object
#       creator might provide a more intuitive approach :)))))))))))))

# TODO: Refactor the code to improve its architecture and adhere to best coding
#       practices. Consider implementing unit tests and using proper design
#       patterns for scalability and maintainability.

# ------------------------------------------------------------------------------
# Code Starts Here
# ------------------------------------------------------------------------------

from typing import Optional

import uvicorn
import graphene
from graphene import relay
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
from fastapi import FastAPI
import asyncio
import httpx


async def get_movies_from_service(query, *args, **kwargs):
    api_key = "c05820ad"
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"http://www.omdbapi.com/?apikey={api_key}&s={query}"
        )
    print(response.json())
    return response.json()


class Movie(graphene.ObjectType):
    class Meta:
        interfaces = (relay.Node, )

    imdbID = graphene.String()
    Title = graphene.String()
    Year = graphene.String()
    Type = graphene.String()
    Poster = graphene.String()


class MovieConnection(relay.Connection):
    class Meta:
        node = Movie

    total_count = graphene.Int()

    def resolve_total_count(root, info):
        return info.context["total_results"]


class Query(graphene.ObjectType):
    movies = relay.ConnectionField(
        MovieConnection,
        Title=graphene.String(),
        ImdbID=graphene.String()
    )

    async def resolve_movies(
        root,
        info,
        Title: Optional[str] = None,
        ImdbID: Optional[str] = None,
        **kwargs
    ):
        if bool(ImdbID) + bool(Title) == 0:
            raise Exception("You must provide a title or imdbID")
        try:
            num_pages = 10
            tasks = [
                get_movies_from_service(query=Title, page=i)
                for i in range(1, num_pages + 1)
            ]
            responses = await asyncio.gather(*tasks)
            movies = [movie for response in responses for movie in response.get('Search', [])]
            info.context.update(
                {"total_results": responses[0].get("totalResults")}
            )
            return movies
        except Exception as err:
            print(err)
            raise err from None


app = FastAPI()
schema = graphene.Schema(query=Query)
app.add_route("/test", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=7777, reload=True)
