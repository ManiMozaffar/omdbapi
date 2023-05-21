from .abc import AbstractCrawler
from .cores import HTTPXCore


class HTTPXBaseCrawler(AbstractCrawler):
    def __init__(self):
        self.core = HTTPXCore()

    async def execute(self, url, params, body, page_num, method): ...
    async def authorize(self): ...
