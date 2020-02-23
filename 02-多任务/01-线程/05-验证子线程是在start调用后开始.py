import threading
import time


def test1():
    for i in range(5):
        print("----test1----%d" % i)
        time.sleep(1)
    # 如果创建Thread时执行的函数运行结束，意味着这个子线程结束。


def main():
    # 在调用Thread之前先打印当前线程信息
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)

    # 在调用Thread之后打印
    t1.start()

    # 在调用start之后打印
    print(threading.enumerate())

    # 结论：
    # 当调用Thread的时候，不会创建线程
    # 当调用Thread类创建出来的实例对象的start方法时，线程才会被创建并且运行


if __name__ == '__main__':
    main()
