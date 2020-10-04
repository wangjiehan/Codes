#求n！的结果
#(1)传统方法（用已知的计算方式去循环）：
def getFactorial1(n):
	res = 1
	for i in range(1, n+1):
		res *= i
	return res
#(2)递归方法（用已知尝试的方式去计算）：
def getFactorial2(n):
	if n == 1:
		return 1
	else:
		res = n * getFactorial2(n-1)
		return res
x = int(input('Please enter the n: '))
print(getFactorial1(x))
print(getFactorial2(x))
