import gevent
import time


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)  # gevent的延时需要调用自己的sleep方法

# 此处print用于验证多任务从哪里开始执行---->  g1.join()
print("---1---")
g1 = gevent.spawn(f, 5)
print("---2---")
g2 = gevent.spawn(f, 5)
print("---3---")
g3 = gevent.spawn(f, 5)
print("---4---")

# gevent无延时，就不执行多任务；有延时的时候才执行多任务
# *核心*：所谓协程，就是利用函数中等待的时间去执行其他的操作
# gevent遇到延时，自己寻找创建的gevent，据此自己管理切换动作
# 在网络编程环境下，会遇到各种阻塞，而发生阻塞时就可以通过gevent的协程切换能力提高性能
g1.join()
g2.join()
g3.join()
