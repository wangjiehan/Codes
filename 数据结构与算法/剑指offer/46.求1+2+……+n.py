'''
46.求1+2+……+n
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
循环要用到for和while，递归要用if
Python特性：利用sum()和range()，还有list()

注意：sum()括号内要加在一起的所有数必须list化成一个数组！
比如sum([1,2,3])
此处是range在sum的括号中的情况，可以把range列表化，也可以不用
'''
def Sum_Solution(n):
	return sum(range(1, n+1))
	#或者  sum(list(range(1, n+1)))
