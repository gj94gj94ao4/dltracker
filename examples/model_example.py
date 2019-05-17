import datetime

import tracker.database as db
from tracker.database.models import *

db.init_db()


w = Work()
w.uid = "RJ231054"
w.name = "催眠スクール～催眠にかかる為の催眠音声～"
w.club = "エロトランス"
w.series = None
w.publish_date = datetime.datetime(2018, 9, 15)

r = Record()
r.dlcount = 5955
r.uid = "RJ231054"
r.favoritecount = 4735
r.timestamp = datetime.datetime(2019, 5, 14, hour=15)  # 之後get需要包含所在時區


sess = db.Session()
sess.add_all([r, w])
sess.commit()
del r, w 

all_works = sess.query(Work).all()
work:Work = all_works[0]

cv1 = CV()
cv1.name = "かの仔"
cv2 = CV()
cv2.name = "陽向葵ゅか"
work.cvs.append(cv1)
work.cvs.append(cv2)
print(sess.dirty)
sess.commit()
