# 求 f(x) = x ** 3 - x - 10 的极值

def f(x):
	return x ** 3 - x - 10

def f_1(x):
	return 3 * (x ** 2) - 1
	
def f_2(x):
	return 6 * x

def NewtonMethodForExtremePoint(f, f_1, f_2):
	x = float(input('Please enter initial x: '))
	while f_1(x) >0.00000001:
		y = f(x)
		y_1 = f_1(x)
		y_2 = f_2(x)
		x = x - y_1 / y_2
	return x

print(NewtonMethodForExtremePoint(f, f_1, f_2))

