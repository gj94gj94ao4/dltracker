from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

import tracker
from tracker import database as db
from tracker.database.models import *

db.engine = create_engine('sqlite:///:memory:', echo=True)
db.Session = sessionmaker(bind=db.engine)
db.init_db()
sess: Session = db.Session()


def test_add():
    tracker.add("RJ231054")
    w: Work = sess.query(Work).one()
    assert w.uid == "RJ231054"


def test_add_no_cvs():
    tracker.add("RJ245995")
    w: Work = sess.query(Work).one()
    assert w.uid == "RJ245995"


def test_record():
    w = Work(uid="RJ231055")
    sess.add(w)
    sess.commit()
    tracker.record(datetime.now(), w)
    n_r: Record = sess.query(Record).one()
    assert n_r.work == w
