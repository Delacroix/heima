num = 100
nums = [11, 22]


def test():
    global num
    num += 100


def test2():
    nums.append(33)    # 可以不加global
    # num += [100, 200]   不加global不行

    # 结论：
    # 在一个函数中对全局变量进行修改时，到底是否需要使用global进行说明
    # 要看是否对全局变量的执行指向进行了修改，
    # 如果修改了执行，即让全局变量指向了一个新的地方，那么必须使用global
    # 如果仅仅是修改了指向的空间中的数据，此时不用使用global


print(num)
print(nums)

test()
test2()

print(num)
print(nums)
