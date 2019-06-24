from tracker.crawler.maniax import ManiaxCrawler

maniax = ManiaxCrawler("RJ231054")
maniax.fetch_work()


def test_get_link():
    assert maniax.get_link(
    ) == "https://www.dlsite.com/maniax/work/=/product_id/RJ231054.html"


def test_get_name():
    assert maniax.get_name() == "催眠スクール～催眠にかかる為の催眠音声～"


def test_get_uid():
    assert maniax.get_uid() == "RJ231054"


def test_get_dl_count():
    assert type(maniax.get_dl_count()) == int
    assert maniax.get_dl_count() >= 5966


def test_get_wishlist_count():
    assert type(maniax.get_wishlist_count()) == int
    assert maniax.get_wishlist_count() >= 4739


def test_get_publish_date():
    assert maniax.get_publish_date() == "2018年09月15日"


def test_get_price():
    assert type(maniax.get_price()) == int


def test_get_cvs():
    assert maniax.get_cvs() == \
        ['かの仔', 'みもりあいの', '陽向葵ゅか', 'あきら',
         '一条ひらめ', 'ユメノシオリ', '山田じぇみ子', '御上みみ', '望(Dose and Dreams)']


def test_get_series():
    assert maniax.get_series() == None
