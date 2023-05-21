from core.crawler import HTTPXBaseCrawler, NotValidPageNumber
from core.config import config
from app.schemas.extras import OMDBResponse


class OMDBApiModel(HTTPXBaseCrawler):
    """OMDB Cralwer, using HTTPX Core"""
    async def execute(
        self,
        params: dict,
        page_num: int,
    ) -> OMDBResponse:
        params = await self.authorize(params)
        params.update(page=page_num)
        if not 0 <= page_num <= 100:
            raise NotValidPageNumber("Page number must be between 0 and 100")
        response = await self.core.get(
            url="http://www.omdbapi.com",
            params=params
        )
        if response.json()["Response"] == 'False':
            return OMDBResponse(totalResults=0, Search=[])
        return OMDBResponse(**response.json())

    async def authorize(self, params: dict) -> dict:
        params["apikey"] = config.OMDB_APIKEY
        return params
