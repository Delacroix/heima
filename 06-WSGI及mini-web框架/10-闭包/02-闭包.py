# 以y=kx+b为例，计算一条线上的各个点 即给出x 计算y

# 第一种方式
# k = 1
# b = 2
# y = k*x+b
# 缺点：多次计算时，需要多次重复写y=k*x+b

# 第二种
def line_2(k, b, x):
	print(k*x+b)

line_2(1, 2, 0)
line_2(1, 2, 1)
line_2(1, 2, 2)
# 缺点：如果想要多次计算y值，每次都要传递k,b值

print("-"*50)

# 第三种：全局变量
k = 1
b = 2
def line_3(x):
	print(k*x+b)

line_3(0)
line_3(1)
line_3(2)
k = 11
b = 22
line_3(0)
line_3(1)
line_3(2)
# 缺点：如果要计算多条线上的y值，需要每次对全局变量进行修改，代码会增多
print("-"*50)
# 第四种：缺省参数
def line_4(x, k=1, b=2):
	print(k*x+b)

line_4(0)
line_4(1)
line_4(2)

line_4(0, k=11, b=22)
line_4(1, k=11, b=22)
line_4(2, k=11, b=22)
# 优点：比全局变量的优势在于--k,b是函数line_4的一部分，而不是全局变量；全局变量可以被其他函数修改
# 缺点：如果要计算多条线上的y值，需要在调用的时候传递参数
print("-"*50)

# 第五种：实例对象
class Line5(object):
	def __init__(self, k, b):
		self.k = k
		self.b = b
	def __call__(self, x):
		print(self.k * x + self.b)

line_5_1 = Line5(1, 2)
line_5_1(0)
line_5_1(1)
line_5_1(2)
line_5_1 = Line5(11, 22)
line_5_1(0)
line_5_1(1)
line_5_1(2)
# 缺点：为了计算多条线上的y值，需要保持多个k,b的值，因此用了很多个实例对象，浪费资源

print("-"*50)
# 第六种：闭包
def line_6(k, b):
	def create_y(x):
		print(k*x+b)
	return create_y

line_6_1 = line_6(1, 2)
line_6_1(0)
line_6_1(1)
line_6_1(2)
line_6_1 = line_6(11, 22)
line_6_1(0)
line_6_1(1)
line_6_1(2)