a = 10
'''
# 报错，函数内，首先决定出现在=左边的a，优先被定义为局部变量，该变量的命名默认覆盖掉外面的全局变量
# 再执行=右边，则会因为a未初始化而报错
def f():
	a = a + 10
	print(a)

f()
print(a)
'''

def f():
	x = a + 10
	print(x)

f()
print(a)


def fx():
	x = a
	print(x)
fx()
print(a)

'''
#
def fx2():
	a = a
	print(a)
fx2()
print(a)
'''

x = [1,2]
def f2(x):
	x.append(1)

f2(x)
print(x)
