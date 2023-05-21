from typing import List
import asyncio
import math

from app.models import OMDBApiModel, OMDBResponse
from core.utils.decorators import capacity_controller


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
            self.get_single_page(page_number=index, query=query)
            for index in _range
        ]
        responses = await asyncio.gather(*tasks)
        return responses

    @capacity_controller(threshold=100)
    def get_max_size(
        self, desired_size: int, total_size: int, per_page: int
    ) -> int:
        result = math.ceil(total_size/per_page)
        if desired_size:
            desired_result = math.ceil(desired_size/per_page)
            if desired_result < result:
                return desired_result
        return result

    async def all(
        self, query: dict, limit: int, skip: int, per_page: int = 10
    ) -> dict:
        start_page = skip // per_page + 1
        skip_on_page = skip % per_page
        result = await self.get_single_page(page_number=1, query=query)

        if (
            result.totalResults > per_page and limit > per_page
        ) or (
            start_page > 1
        ):
            last_page_num = self.get_max_size(
                desired_size=limit,
                total_size=result.totalResults/per_page,
                per_page=per_page
            )
            responses = await self.get_range_pages(
                _range=range(
                    start_page,
                    last_page_num + 1
                ),
                query=query
            )
            combined_search = [
                result for response in responses for result in response.Search
            ]
            total_results = (
                responses[0].totalResults if len(responses) > 0
                else result.totalResults
            )
            result = OMDBResponse(
                Search=combined_search,
                totalResults=total_results,
            )
        try:
            result.Search = result.Search[skip_on_page:(skip_on_page+limit)]
        except IndexError:
            """We ignore this exception, which means result is empty"""
        return result.dict(exclude_unset=True)
