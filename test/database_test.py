import datetime

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from tracker import database as db
from tracker.database.models import *

db.engine = create_engine('sqlite:///:memory:', echo=True)
db.init_db()
sess: Session = db.Session()


def gen_work(index) -> Work:
    w = Work()
    w.rjnumber = ["RJ231054", "RJ226361"][index]
    w.name = ["催眠スクール～催眠にかかる為の催眠音声～",
              "射精させてくれない?! 自動手淫人形の耳舐めと淫語と手コキと寸止め - 痴女ドール フレデリカ -【超高音質バイノーラル】"][index]
    w.club = ["エロトランス", "VOICE LOVER"][index]
    w.series = [None, "自動手淫人形"][index]
    w.publish_data = [datetime.datetime(
        2018, 9, 15), datetime.datetime(2018, 5, 26)][index]
    return w


def gen_cv(index) -> CV:
    LIST = ['かの仔', 'みもりあいの', '陽向葵ゅか', 'あきら']
    c = CV()
    c.name = LIST[index % 4]
    return c


def test_Work_storage():
    w = gen_work(0)
    sess.add(w)
    assert w == sess.query(Work).first()
    sess.rollback()


def test_Work_with_CV():
    w = gen_work(0)
    cvs = [gen_cv(0), gen_cv(1)]

    w.cvs.append(cvs[0])
    w.cvs.append(cvs[1])
    sess.add(w)
    retire_work: Work = sess.query(Work).first()
    assert cvs[0] == retire_work.cvs[0] and cvs[1] == retire_work.cvs[1]
    sess.rollback()


def test_CV_with_Work():
    cv = gen_cv(0)
    works = [gen_work(0), gen_work(1)]
    cv.works.append(works[0])
    cv.works.append(works[1])
    sess.add(cv)
    retire_cv: CV = sess.query(CV).first()
    assert retire_cv.works[0].rjnumber == "RJ231054" and retire_cv.works[1].rjnumber == "RJ226361"
    sess.rollback()
