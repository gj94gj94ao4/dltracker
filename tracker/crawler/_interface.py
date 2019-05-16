from datetime import datetime
from typing import List


class DLCrawler():

    def get_link(self) -> str:
        return self.link

    def get_name(self) -> str:
        return self.name

    def get_rjnumber(self) -> str:
        return self.rjnumber

    def get_dl_count(self) -> int:
        return self.dl_count

    def get_wishlist_count(self) -> int:
        return self.wishlist_count

    def get_publish_date(self) -> datetime:
        return self.publish_date

    def get_price(self) -> int:
        return self.price

    def get_cvs(self) -> List[str]:
        return self.cvs

    def get_series(self) -> str:
        return self.series
