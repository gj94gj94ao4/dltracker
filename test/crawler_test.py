from tracker.crawler.maniax import ManiaxCrawler

crawler = ManiaxCrawler("RJ231054")
crawler.fetch_work()


def test_get_link():
    assert crawler.get_link(
    ) == "https://www.dlsite.com/maniax/work/=/product_id/RJ231054.html"


def test_get_name():
    assert crawler.get_name() == "催眠スクール～催眠にかかる為の催眠音声～"


def test_get_uid():
    assert crawler.get_uid() == "RJ231054"


def test_get_dl_count():
    assert type(crawler.get_dl_count()) == int
    assert crawler.get_dl_count() >= 5966


def test_get_wishlist_count():
    assert type(crawler.get_wishlist_count()) == int
    assert crawler.get_wishlist_count() >= 4739


def test_get_publish_date():
    assert crawler.get_publish_date() == "2018年09月15日"


def test_get_price():
    assert type(crawler.get_price()) == int


def test_get_cvs():
    assert crawler.get_cvs() == \
        ['かの仔', 'みもりあいの', '陽向葵ゅか', 'あきら',
         '一条ひらめ', 'ユメノシオリ', '山田じぇみ子', '御上みみ', '望(Dose and Dreams)']


def test_get_series():
    assert crawler.get_series() == None
