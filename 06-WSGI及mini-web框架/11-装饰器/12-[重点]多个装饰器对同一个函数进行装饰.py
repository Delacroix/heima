def add_qx(func):
	print("---开始进行装饰权限1的功能---")
	def call_func(*args, **kwargs):
		print("--这是权限验证1--")
		# func(args, kwargs)  # 不行，相当于传递了2个参数：1个元组，1个字典
		return func(*args, **kwargs)  # 拆包
	return call_func


def add_xx(func):
	print("---开始进行装饰xxx的功能---")
	def call_func(*args, **kwargs):
		print("--这是xxx的功能--")
		return func(*args, **kwargs)
	return call_func

@add_qx  # 等价于 test1 = add_qx(test1),此处右边的test1已经指向了add_xx内的闭包；所以add_qx的func参数也指向该闭包
@add_xx  # 等价于 test1 = add_xx(test1)
def test1():
	print("---test1---")


test1()

# 装饰器 装饰阶段：先装下面的，后装上面的
# 执行阶段，谁先装饰，先执行谁