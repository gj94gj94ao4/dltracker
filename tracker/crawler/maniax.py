import requests
import json
import asyncio
from lxml import etree

from . import HEADERS
from ._abstract import DLCrawler


class ManiaxCrawler(DLCrawler):

    def __init__(self, uid: str):
        self.uid = uid
        self.link = f"https://www.dlsite.com/maniax/work/=/product_id/{uid.upper()}.html"
        self.info_url = f"https://www.dlsite.com/maniax/product/info/ajax?product_id={self.uid.upper()}&cdn_cache_min=1"

    def fetch_work(self):
        self.body_response = requests.get(self.link, headers=HEADERS)
        self.info_response = requests.get(self.info_url, headers=HEADERS)
        self._parse_body()
        self._parse_work_info()

    def fetch_work_record(self):
        self.info_response = requests.get(self.info_url, headers=HEADERS)
        self._parse_work_info()

    def _parse_work_info(self):
        jres = json.loads(self.info_response.text)
        jres = jres[self.uid]
        self.dl_count = int(jres['dl_count'])
        self.wishlist_count = int(jres['wishlist_count'])
        self.price = jres['price']

    def _parse_body(self):
        self.html = etree.fromstring(
            self.body_response.text, etree.HTMLParser())
        outline_element = self.html.xpath('//table[@id="work_outline"]')[0]
        self.publish_date = None
        self.cvs = []
        self.series = ""
        for e in outline_element.xpath('tr'):
            key = e.xpath('th')[0].text
            if key == '販売日' or key == "販賣日":
                self.publish_date = e.xpath('td/a')[0].text
            elif key == '声優':
                self.cvs = [e.text for e in e.xpath('td/a')]
            elif key == 'シリーズ名':
                self.series = e.xpath('td/a')[0].text
        self.name = self.html.xpath('//*[@id="work_name"]/a')[0].text
        self.club = self.html.xpath('//*[@id="work_maker"]/tr/td/span/a')[0].text
