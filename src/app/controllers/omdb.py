from typing import Optional

import graphene

from app.schemas.graph import MovieConnection
from app.repositories.omdb import OMDBRepository


class OMDBController(graphene.ObjectType):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.repository = OMDBRepository()

    movies = graphene.relay.ConnectionField(
        MovieConnection,
        Title=graphene.NonNull(graphene.String),
        Type=graphene.String()
    )

    @staticmethod
    def exclude_none(_dict: dict):
        return {
            key: value for key, value in _dict.items()
            if value is not None
        }

    @staticmethod
    def create_query(query: dict):
        query = {
            "s": query.get("Title"),
            "type": query.get("Type"),
            "y": query.get("Year")
        }
        return OMDBController.exclude_none(query)

    async def resolve_movies(
        root,
        info,
        Title: str,
        Year: Optional[str] = None,
        Type: Optional[str] = None,
        **kwargs
    ):
        query = root.create_query(
            {
                "Type": Type,
                "Title": Title,
                "Year": Year
            }
        )
        result = await root.repository.all(
            query=query,
        )
        return result
