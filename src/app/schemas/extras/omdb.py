import pydantic
from typing import List, Union


class SearchResult(pydantic.BaseModel):
    imdbID: str
    Title: str
    Year: Union[str, None]
    Type: str
    Poster: Union[str, None]


class OMDBResponse(pydantic.BaseModel):
    Search: List[SearchResult]
    totalResults: str
