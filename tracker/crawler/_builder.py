import re

from .maniax import ManiaxCrawler
from ._abstract import DLCrawler


class DLCrawlerBuilder():

    def __init__(self):
        self.uid: str = None

    def set_uid(self, uid: str):
        self.uid = uid
        return self

    def build(self) -> DLCrawler:
        if self.uid:
            self.uid = self.uid.upper()
            if re.match(r'RJ\d{1,8}', self.uid):
                return ManiaxCrawler(self.uid)
        raise Exception("no matched Crawler class")
