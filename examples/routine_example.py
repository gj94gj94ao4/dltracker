import time
from sched import scheduler
from datetime import datetime
from multiprocessing import Process

def mot():
    print("run!!")
    s.enter(3600, 1, mot)

def te():
    time.sleep(5)    
    print('te run!!')

d = datetime.now()
next_ = datetime(d.year, d.month, d.day, d.hour + 1)
s = scheduler(time.time)
s.enter(5, 1, mot)
# s.enterabs(time.mktime(next_.timetuple()), 1, mot)
s.run(False)
p = Process(target=te)
p.start()
print()
