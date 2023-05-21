from typing import List
import asyncio
import math

from app.models import OMDBApiModel, OMDBResponse


class OMDBRepository:
    def __init__(self):
        self.model_class = OMDBApiModel()

    async def get_single_page(
        self, page_number: int, query: dict
    ) -> OMDBResponse:
        return await self.model_class.execute(
            page_num=page_number, params=query
        )

    async def get_range_pages(
        self, _range: range, query: dict
    ) -> List[OMDBResponse]:
        tasks = [
            self.get_single_page(page=index, query=query)
            for index in range(1, _range)
        ]
        responses = await asyncio.gather(*tasks)
        return responses

    async def all(
        self, query: dict, size: int = 10_000, per_page: int = 5
    ) -> OMDBResponse:
        result = await self.get_single_page(page_number=1, query=query)

        if result.totalResults > per_page and size > per_page:
            responses = await self.get_range_pages(
                _range=range(
                    1,
                    (math.ceil(result.totalResults/per_page) + 1)
                ),
                query=query
            )
            combined_search = [
                result for response in responses for result in response.Search
            ]
            result = OMDBResponse(
                Search=combined_search, totalResults=responses[0].totalResults
            )

        return result
