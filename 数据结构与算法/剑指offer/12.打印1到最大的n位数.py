'''
12.打印1到最大的n位数
防止n很大，会导致溢出，这是题目设置的陷阱。
可以把问题转换成数字排列问题，用递归让代码更简洁。
但是，python中已经对大整数可以进行自动转换了，所以不需要考虑大整数溢出问题
'''
def printMax(n):
	for i in range(1, 10**n):
		print(i)
if __name__ == '__main__':
	n = int(input('Enter n: '))
	printMax(n)
