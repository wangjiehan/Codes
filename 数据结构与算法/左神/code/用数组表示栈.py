initSize=int(input('Please enter the size of stack: '))
index=0
arr=[]
def stack_push(a):		#压栈操作，压入a
	global index,initSize		#把函数里的局部变量转化成全局变量
	if index == initSize:
		print('The stack is full. ')
	arr.append(a)
	print(arr[index])
	index += 1
	print(arr)
def stack_pop():		#弹栈操作
	global index,initSize
	if index == 0:
		print('The stack is empty. ')
	print(arr[index-1])
	arr.pop()
	index -= 1
	print(arr)
stack_push(1)
stack_push(3)
stack_pop()
