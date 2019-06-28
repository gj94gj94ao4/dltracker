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
        w.publish_date = datetime.strptime(
            c.get_publish_date()[:11], "%Y年%m月%d日")
        sess.add(w)
        sess.commit()
    else:
        return f'work exist: {result}'
    sess.close()
    return f'{uid} has added.'


def record(datetime_: datetime, uid: str):
    sess = db.Session()
    try:
        sess.query(Work).filter(Work.uid == uid).one()  # Check work exist
    except NoResultFound:
        raise Exception("沒有這個work拉")
    c = DLCrawlerBuilder().set_uid(uid).build()
    c.fetch_work_record()
    r = Record()
    r.uid = c.get_uid()
    r.dl_count = c.get_dl_count()
    r.wishlist_count = c.get_wishlist_count()
    r.timestamp = datetime_
    sess.add(r)
    sess.commit()
    sess.close()


def _delete(uid: str):
    sess = db.Session()
    result = sess.query(Work).filter(Work.uid == uid).one()
    sess.delete(result)
    sess.commit()
    sess.close()
    return f'{uid} has deleted.'


def update(uid: str):
    _delete(uid)
    add(uid)
    return f"{uid} has renewed."


def get_work(uid: str) -> Work:
    sess = db.Session()
    result = sess.query(Work).filter(Work.uid == uid).one_or_none()
    return result
