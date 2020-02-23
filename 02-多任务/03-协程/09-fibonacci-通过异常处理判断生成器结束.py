def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么它就不再是函数，而是一个生成器模板
        a, b = b, a+b
        current_num += 1
    return "ok..."


# 如果在调用create_num的时候，发现这个函数中有yield，那么此时不是调用函数，而是创建一个生成器对象
obj2 = create_num(50)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        # 想要得到生成器的返回值，需要通过异常捕获.value来获取
        print(ret.value)
        break
