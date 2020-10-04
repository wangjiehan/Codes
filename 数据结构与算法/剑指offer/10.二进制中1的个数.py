'''
10.二进制中1的个数
把一个整数n减1，是把二进制下最右边的1变成0，再右边如果存在则所有的0变成1，
而左边的所有位保持不变
n和n-1做与运算，则会把最右边的1开始向右所有位置都变成0，左边保持不变
从右向左遇到一个1就能变一次，当n不为空时，有多少个1就能做多少次位运算
位运算：与（&）、或（|）、异或（^）、取反（~）
'''
def countN1(n):
	count = 0
	if n < 0:			#若为负数，要和0xffffffff相与，消除负数的影响
		n = n & 0xffffffff
	while n:
		n = n & (n-1)
		count += 1
	return count
#python特性解法
def countN2(n):
	return bin(n&0xffffffff).count('1')	#bin()函数把整型转换成二进制字符串
if __name__ == '__main__':
	n = int(input('Enter n: '))
	print(countN1(n))
	print(countN2(n))	
