import re

from .maniax import ManiaxCrawler
from ._abstract import DLCrawler


class DLCrawlerBuilder():

    def __init__(self):
        self.rjnumber: str = None

    def set_rjnumber(self, rjnumber: str):
        self.rjnumber = rjnumber
        return self

    def build(self) -> DLCrawler:
        if self.rjnumber:
            self.rjnumber = self.rjnumber.upper()
            if re.match(r'RJ\d{1,8}', self.rjnumber):
                return ManiaxCrawler(self.rjnumber)
        raise Exception("no matched Crawler class")
