from core.exceptions import BaseCustomException


class BaseCrawlerException(BaseCustomException):
    ...


class NotValidPageNumber(BaseCrawlerException):
    """Page number must be in range 0 through 100"""
