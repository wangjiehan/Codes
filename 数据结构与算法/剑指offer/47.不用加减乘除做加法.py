'''
47.不用加减乘除做加法
写一个函数,求两个整数之和
方法（1）：python特性，调用sum()函数
方法（2）：使用位运算
三步走策略：
(a)只做各位相加不进位（可以用异或来处理，和异或结果相同）：sum
(b)进位：可以想象为两个数先做位与运算，然后整体左移一位(<< 1)：carry
(c)把前两个步骤的结果相加，重复前两步，直到不产生进位为止。
在Python中做位运算，需要做越界检查。

0x7FFFFFFF：
是最大的整型数int（类似于整型正无穷）。二进制表示中，除了首位是 0，其余都是1。
二进制为：01111111 11111111 11111111 11111111
0xFFFFFFFF：
是一个负数的补码，实际代表-1（类似于正负数划分点）。二进制表示中，所有位都是1。
二进制为：11111111 11111111 11111111 11111111
0x80000000：
是最小的整型数int（类似于整型负无穷）。
二进制为：01000000 00000000 00000000 00000000

在Python中做位运算，特有的越界检查：
if num1 < 0x7fffffff:
	return num1
else:
	return ~(num1 ^ 0xffffffff)		#越界时固定写法
'''
#方法（1）
def Add1(num1, num2):
	return sum([num1, num2])

#方法（2）
def Add2(num1, num2):
	while num2:
		sum = (num1 ^ num2) & 0xffffffff	#与上0xffffffff消除负数影响
		carry = ((num1 & num2) << 1) & 0xffffffff
		num1 = sum
		num2 = carry		#相当于不停地把num2上的成分往num1上移	
	if num1 < 0x7fffffff:	#在Python中做位运算，需要做越界检查
		return sum
	else:
		return ~(sum ^ 0xffffffff)	#越界时固定写法
				
if __name__ == '__main__':
	print(Add1(3,5))
	print(Add2(3,5))
		
