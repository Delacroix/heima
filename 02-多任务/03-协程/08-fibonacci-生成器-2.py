def create_num(all_num):
    print("---1---")
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print("---2---")
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么它就不再是函数，而是一个生成器模板
        print("---3---")
        a, b = b, a+b
        current_num += 1
        print("---4---")


# 如果在调用create_num的时候，发现这个函数中有yield，那么此时不是调用函数，而是创建一个生成器对象
obj = create_num(10)

# yield a 的值是多少，此处返回值就是多少
ret = next(obj)
print("obj:", ret)
# 迭代过后的yield a值
ret = next(obj)
print("obj:", ret)

# 创建第二个生成器
obj2 = create_num(2)
ret = next(obj2)
print("obj2:", ret)

# 混入第一个生成器
ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)

ret = next(obj)
print("obj:", ret)


# 生成器一定可以迭代
# num的值由 函数中的 yield 的 a 提供
# for循环执行到yield就暂停，重新开始循环
# for num in obj:
#     print(num)
