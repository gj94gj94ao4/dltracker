import requests
import json
import asyncio
from lxml import etree

from . import HEADERS
from ._interface import DLCrawler


class ManiaxCrawler(DLCrawler):

    def __init__(self, rjnumber: str):
        self.rjnumber = rjnumber
        self.link = f"https://www.dlsite.com/maniax/work/=/product_id/{rjnumber.upper()}.html"
        

    def fetch_work(self):
        info_url = f"https://www.dlsite.com/maniax/product/info/ajax?product_id={self.rjnumber.upper()}&cdn_cache_min=1"
        body_url = self.link
        self.body_response = requests.get(body_url, headers=HEADERS)
        self.info_response = requests.get(info_url, headers=HEADERS)
        self._parse_body()
        self._parse_work_info()

    def fetch_work_record(self):
        self.info_response = requests.get(self.info_url, headers=HEADERS)
        self._parse_work_info()

    def _parse_work_info(self):
        jres = json.loads(self.info_response.text)
        jres = jres[self.rjnumber]
        self.dl_count = int(jres['dl_count'])
        self.wishlist_count = int(jres['wishlist_count'])
        self.price = jres['price']

    def _parse_body(self):
        self.html = etree.fromstring(
            self.body_response.text, etree.HTMLParser())
        outline_element = self.html.xpath('//table[@id="work_outline"]')[0]
        self.publish_date = None
        self.cvs = None
        self.series = None
        for e in outline_element.xpath('tr'):
            key = e.xpath('th')[0].text
            if key == '販売日':
                self.publish_date = e.xpath('td/a')[0].text
            elif key == '声優':
                self.cvs = [e.text for e in e.xpath('td/a')]
            elif key == 'シリーズ名':
                self.series = e.xpath('td/a')[0].text
        self.name = self.html.xpath('//*[@id="work_name"]/a')[0].text
        self.club = self.html.xpath('//*[@id="work_maker"]/tr/td/span/a')[0].text