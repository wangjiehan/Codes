'''
21.包含min函数的栈
栈用数组表示，push()两个栈同时push，pop两个栈同时pop
定义两个栈，第一个是正常压数的stack栈，第二个栈顶记录最小值的min栈，
先把第一个数同时分别压入两个栈中，之后出的每个数先压入第一个栈，再
将当前压入数和min栈的当前栈顶的数比较：
（1）若大于等于min栈当前栈顶且当前栈不为空，则在min栈中重复压入一个min栈当前栈顶的数；
（2）若小于min栈当前栈顶或者当前栈为空，则将当前数压入min栈。
直到stack栈压完，此时min栈栈顶就是最小值。
主要在于push()压栈函数的定义上，区别处理两个栈

'''
class MyStack():
	def __init__(self):
		self.stack = []
		self.minstack = []
	def push(self, val):		#同时弹，同时压
		self.stack.append(val)
		if self.minstack and self.minstack[-1] <= val:	#minstack不为空不能少
			self.minstack.append(self.minstack[-1])
		else:		#minstack为空或者压入的数比minstack栈顶的数要小
			self.minstack.append(val)	
	def pop(self):
		if self.stack == [] or self.minstack == []:
			return None
		self.stack.pop()
		self.minstack.pop()
	def min(self):
		if self.minstack:
			return self.minstack[-1]
		else:
			return None
