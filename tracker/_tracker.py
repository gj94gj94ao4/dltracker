from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from . import database as db
from .database.models import Work, Record, CV
from .crawler import DLCrawlerBuilder


def add(uid: str):
    sess = db.Session()
    result = sess.query(Work).filter(Work.uid == uid).one_or_none()

    if not result:
        c = DLCrawlerBuilder().set_uid(uid).build()
        c.fetch_work()
        w = Work()
        w.uid = c.get_uid()
        w.name = c.get_name()
        w.club = c.get_club()
        w.series = c.get_series()
        for cv_name in c.get_cvs():
            cv = sess.query(CV).filter(CV.name == cv_name).one_or_none()
            if not cv:
                cv = CV(name=cv_name)
            w.cvs.append(cv)
        w.publish_date = datetime.strptime(c.get_publish_date(), "%Y年%m月%d日")
        sess.add(w)
        sess.commit()
    else:
        return f'work exist: {result}'
    sess.close()
    return f'work {uid} fetch finish.'


def record(datetime_: datetime, work: Work):
    sess = db.Session()
    try:
        sess.query(Work).filter(Work.uid == work.uid).one()  # Check work exist
    except NoResultFound:
        raise Exception("沒有這個work拉")
    c = DLCrawlerBuilder().set_uid(work.uid).build()
    c.fetch_work_record()
    r = Record()
    r.uid = c.get_uid()
    r.dl_count = c.get_dl_count()
    r.wishlist_count = c.get_wishlist_count()
    r.timestamp = datetime_
    sess.add(r)
    sess.commit()
    sess.close()
