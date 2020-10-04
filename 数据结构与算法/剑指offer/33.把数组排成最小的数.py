'''
33.把数组排成最小的数
方法（1）：暴力全排列，再比较出最小的数。调用itertools包里的permutations()方法
		  ''.join(arr)：是把数组arr里所有元素连接成字符串。（join后面跟的是数组）
方法（2）：
	将数字转换为字符串后进行自定义排序（使得按照字符串拼接的从小到大的顺序排列）
	转字符串的目的是因为字符串比较大小可以补位，复合题意
	根据题目要求，转化为字符拼接更方便。
	字典序比较的原理（左神）

设计比较大小的规则为 若 ab > ba 则b应该在a前面。cmpStr(x,y) 函数用于比较：
如果 x < y 返回负数，不动；如果 x == y 返回 0；如果 x > y 返回正数，交换位置。
注：
python3.0里sort、sorted去掉了cmp参数，只能调用functools包里cmp_to_key()方法
''' 
import itertools
import functools
#方法（1）：O(N!)
def PrintMinNumber1(numbers):
	if not numbers:
		return None
	str_numbers = [str(i) for i in numbers] 	#列表解析
	permu = itertools.permutations(str_numbers)	#字符串元素的全排列（二维数组）
	res = [int(''.join(i)) for i in permu]		#把每种排列，即一维分数组i里的单个字符元素连起来
	return min(res)
#方法（2）：O(NlogN)	
def PrintMinNumber2(numbers):
	if not numbers:
		return None
	str_numbers = [str(i) for i in numbers]		#转化为字符
	res = sorted(str_numbers, key=functools.cmp_to_key(cmpStr))
	return ''.join(res)
def cmpStr(a, b):
	return int(str(a)+str(b)) - int(str(b)+str(a))
	
	
if __name__ == '__main__':
	print(PrintMinNumber1([321,12,3]))
	print(PrintMinNumber2([321,12,3]))
'''
lambda指匿名函数。形式如下：
lambda 参数1,参数2 : 函数
'''

