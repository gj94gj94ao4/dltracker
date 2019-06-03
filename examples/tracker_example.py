import tracker
from datetime import datetime


tracker.add("RJ231054")
tracker.add("RJ226361")

sess = tracker.database.Session()

ws = sess.query(tracker.Work).all()

now = datetime.now()
for work in ws:
    tracker.record(now, work)

#### display

print(sess.query(tracker.Work).all())
[print(r) for r in sess.query(tracker.Record).all()]

