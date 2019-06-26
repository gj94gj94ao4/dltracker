import time
from datetime import datetime
from sched import scheduler
from typing import List

from ._tracker import record
from .database.models import Work
from . import database as db

sess = db.Session()
WORK_LIST = [workuid.uid for workuid in sess.query(db.models.Work.uid).all()]
sess.close()
s = scheduler(time.time)


def _task():
    sess = db.Session()
    work_list = [workuid.uid for workuid in sess.query(db.models.Work.uid).all()]
    sess.close()
    print(f"record start!! with {work_list}")
    now = datetime.now()
    for work in work_list:
        print(f"in work {work}")
        record(now, work)
    print('rocord finish!!')
    s.enter(3600, 1, _task)


def run():
    d = datetime.now()
    next_ = datetime(d.year, d.month, d.day, d.hour + 1)
    # s.enter(5, 1, _task)
    s.enterabs(time.mktime(next_.timetuple()), 1, _task)
    s.run()

def show():
    while True:
        time.sleep(2)
        print(WORK_LIST)
