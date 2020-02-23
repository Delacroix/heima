def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print(">>>ret>>>", ret)
        a, b = b, a+b
        current_num += 1


obj = create_num(10)

obj.send(None)  # send一般不会放到第一次启动生成器，如果非要这么做，需要传递None

# 第一次调用next，只执行了等号左边的yield， 把a的值传给了next
ret = next(obj)
print(ret)

# send里面的数据会传递到第5行， 当做yield a 的结果，然后由ret保存这个结果
ret = obj.send('hahaha')
print(ret)

ret = obj.send('hahaha')
print(ret)

ret = obj.send('hahaha')
print(ret)
