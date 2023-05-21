import pydantic
from typing import List, Union, Optional


class SearchResult(pydantic.BaseModel):
    imdbID: str
    Title: str
    Year: Union[str, None]
    Type: str
    Poster: Union[str, None]


class OMDBResponse(pydantic.BaseModel):
    Search: List[SearchResult]
    totalResults: int
    Response: Optional[bool]
