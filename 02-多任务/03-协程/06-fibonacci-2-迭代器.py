import time


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_nums = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_nums:
            ret = self.a

            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1

            return ret
        else:
            # 自定义一个用于停止迭代的异常
            raise StopIteration


fibo = Fibonacci(10)


for num in fibo:
    print(num)
    time.sleep(1)
