'''
34.丑数:只包含因子2、3、5的数，求按从小到大顺序的第n个丑数
例如6、8都是丑数，14不是。1是第一个丑数。
方法（1）：逐个判断每个整数是不是丑数。（效率太低！！）
一个数，若能被2整除，则连续除以2；若能被3整除，连续除以3；若能被5整除，连续除以5。
如果到最后得到的是1，此数为丑数，否则不是。
方法（2）：创建数组保存已经找到的丑数，用空间换时间。
思路：
丑数一定是另一个丑数乘以2、3或5的结果（1除外），按顺序保存已知的丑数，
下一个丑数，一定是某三个已知的丑数乘以2，3，5后，所得到三个大于当前最大丑数的乘积中，
最小值
'''
#方法（1）：
def getUglyNumber1(n):
	if n <= 0:
		return None
	if n == 1:
		return 1
	number = 0
	count = 0
	while count < n:
		number += 1
		if IsUgly(number):
			count += 1
	return number
def IsUgly(number):
	while number % 2 == 0:
		number /= 2
	while number % 3 == 0:
		number /= 3
	while number % 5 == 0:
		number /= 5
	if number == 1:
		return True
	return False
#方法（2）：t2、t3、t5记录已有丑数数组内乘上2、3、5后会大于当前最大丑数的坐标
def getUglyNumber2(n):
	if n <= 0:
		return None
	ugly = [1]
	count = 1
	t2, t3, t5 = 0, 0, 0
	while count < n:
		while 2 * ugly[t2] <= ugly[-1]:			#注意'='
			t2 += 1
		while 3 * ugly[t3] <= ugly[-1]:
			t3 += 1
		while 5 * ugly[t5] <= ugly[-1]:
			t5 += 1
		ugly.append(min(2*ugly[t2], 3*ugly[t3], 5*ugly[t5]))
		count += 1
	return ugly
if __name__ == '__main__':
	print(getUglyNumber1(11))
	print(getUglyNumber2(11))

