from core.crawler import HTTPXBaseCrawler, NotValidPageNumber
from core.config import config
from schemas.extras import OMDBResponse


class OMDBApiModel(HTTPXBaseCrawler):
    async def execute(
        self,
        params: dict,
        page_num: int,
    ):
        params = await self.authorize(params)
        params.update(page=page_num)
        if not 0 <= page_num <= 100:
            raise NotValidPageNumber("Page number must be between 0 and 100")
        response = await self.core.get(
            url="http://www.omdbapi.com",
            params=params
        )
        return OMDBResponse(response.json())

    async def authorize(self, params: dict):
        params["apikey"] = config.OMDB_APIKEY
        return params
