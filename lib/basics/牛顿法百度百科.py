# 求 f(x) = x ** 3 + x - 10 的零点

def f(x):
	return x ** 3 + x - 10

def f_1(x):
	return 3 * (x ** 2) + 1

def NewtonMethodForZeroPoint(f, f_1):
	x = float(input('Please enter initial x: '))
	while f(x) > 0.00000001 or f(x) < -0.00000001:
		y = f(x)
		y_1 = f_1(x)
		x = x - y / y_1
	return x

print(NewtonMethodForZeroPoint(f, f_1))
