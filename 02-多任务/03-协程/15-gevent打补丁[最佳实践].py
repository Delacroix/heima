import gevent
import time
from gevent import monkey


monkey.patch_all()


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)  # monkey.patch_all 将会把代码中所有耗时的地方换成 gevent 的方法来实现


# joinall 把创建的对象装入字典，一起执行后再结束
gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 5),
    gevent.spawn(f, 5)
])
