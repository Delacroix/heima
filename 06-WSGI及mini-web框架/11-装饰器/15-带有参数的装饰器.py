def set_level(level_num):	
	def set_func(func):
		def call_func(*args, **kwargs):
			if level_num == 1:
				print("---权限级别1验证---")
			elif level_num == 2:
				print("---权限级别2验证---")
			return func()
		return call_func
	return set_func

# 1、装饰器带参数时，调用set_level并且将1当作实参传递，用于保存参数；
# 2、返回set_func，当作装饰器对test1函数进行装饰，用于保存test1函数的引用;
# 3、用于调用call_func的返回值，执行该闭包内的操作
@set_level(1)  
def test1():
	print("---test1---")
	return "ok"

@set_level(2)
def test2():
	print("---test2---")
	return "ok"

test1()
test2()