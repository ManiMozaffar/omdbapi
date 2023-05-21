from typing import Optional, List

import graphene

from app.schemas.graph import MovieConnection
from app.repositories.omdb import OMDBRepository


class OMDBController(graphene.ObjectType):
    """Controller for OMDB GraphQL API Interface"""

    movies = graphene.relay.ConnectionField(
        MovieConnection,
        Title=graphene.NonNull(graphene.String),
        Type=graphene.String(),
        Year=graphene.String(),
        Skip=graphene.Int(),
        Limit=graphene.Int()
    )

    @staticmethod
    def exclude_none(_dict: dict) -> dict:
        return {
            key: value for key, value in _dict.items()
            if value is not None
        }

    @staticmethod
    def create_query(query: dict) -> dict:
        """Resolves query parameters for API"""
        query = {
            "s": query.get("Title"),
            "type": query.get("Type"),
            "y": query.get("Year")
        }
        return OMDBController.exclude_none(query)

    async def resolve_movies(
        root,
        info: graphene.ResolveInfo,
        Title: str,
        Year: Optional[str] = None,
        Type: Optional[str] = None,
        Skip: Optional[str] = None,
        Limit: Optional[str] = None,
        **_
    ) -> List[dict]:
        if Limit is None:
            Limit = 20
        if Skip is None:
            Skip = 0

        query = OMDBController.create_query(
            {
                "Type": Type,
                "Title": Title,
                "Year": Year
            }
        )
        result = await OMDBRepository().all(
            query=query,
            limit=Limit,
            skip=Skip
        )
        info.context.update(total_counts=result.get("totalResults"))
        return result.get("Search")
