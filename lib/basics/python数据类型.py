"""
python3不可变类型
	Number(数字int、float)
	String(字符串)
	Tuple (元组)
python3可变类型
	List(列表)
	Dictionary (字典)
	Sets(集合)
	
因为hash的key必须是不可变，因此字典中的key只能为 数字、字符串、元组
"""
# 列表list、字典dict、集合set，这些可变类型都是引用传递
a = [1,2]
b = a
a.append(3)
print(a)
print(b)

c = {}

# 单个值int float、字符串string、元组tuple，这些不可变类型都是值传递
x = 1.1
y = x
x += 1
print(x)
print(y)

s = "abc"

def fun1(a):
	a.append(10)

def fun3(c):
	c[1] = "b"

def fun2(x):
	x += 1

def fun4(s):
	s += "d"

# a初始为[1,2]，变为[1,2,10]
fun1(a)
print(a)

# c初始为{}，变为 {1:"b"}
fun3(c)
print(c)

# x初始为2，没变化
fun2(x)
print(x)

# s初始为"abc"，没变化
fun4(s)
print(s)

# python函数内局部变量会自动寻找全局变量，但不可变类型的局部变量得通过 return 传出来
def pri():
	print(a)
	print(c)
	print(x)
	print(s)
pri()

def test():
	tmp = x
test()
