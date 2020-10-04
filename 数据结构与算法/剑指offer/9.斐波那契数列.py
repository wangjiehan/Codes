'''
9.斐波那契数列
方法（3）：
[[f(n), 	f(n-1)],	[[1, 1]	^ (n-1)
 [f(n-1),	f(n-2)]	= 	 [1, 0]] 
'''
import numpy as np
#递归法（效率极低）：
def f1(n):
	if n == 0:
		return 0
	if n == 1 or n == 2:
		return 1
	return f1(n-1) + f1(n-2)
#动态规划，迭代法
def f2(n):
	arr = [0,1,1]	
	for i in range(3, n+1):
		tmp = arr[i-1] + arr[i-2]
		arr.append(tmp)		#新的数直接存进数组
	return arr[n]
#矩阵乘方法：
def f3(n):
	tmp = [[1,1],
		   [1,0]]
	arr = [[1,0],
		   [0,1]]
	if n == 0:
		return 0
	elif n == 1:
		return 1
	for i in range(0, n-1):
		arr = np.dot(arr, tmp)
	return arr[0][0]
if __name__ == '__main__':
	n = int(input('Enter n: '))
	print(f1(n))
	print(f2(n))
	print(f3(n))
