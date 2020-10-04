initSize=int(input('Please enter the size of queue: '))
size=0
start=0
end=0
arr=['']*initSize
def queue_push(a):		#入队操作
	global size,start,end,initSize	#把函数里的局部变量转化成全局变量
	if size < initSize:
		if end < initSize-1:
			arr[end]=a
			end += 1
			size += 1
		else:			#如果end指针已到最底，再入队就跳至最前的0位置
			arr[end]=a
			end = 0
			size += 1
	print(arr)
	print(start,end,size)
	if size == initSize:
		print('The queue is full. ')
def queue_poll():		#出队操作
	global size,start,end,initSize
	if size == 0:
		print('The queue is empty. ')
	if start < initSize-1:
		print(arr[start])
		arr[start]=''
		start += 1
		size -= 1
	else:			#如果start指针已到最底，再出队就跳至最前的0位置
		print(arr[start])
		arr[start]=''
		start = 0
		size -= 1
	print(arr)
	print(start,end,size)
queue_push(3)
queue_push(4)
queue_push(5)
queue_push(6)
queue_poll()
queue_push(7)
queue_poll()
queue_poll()
