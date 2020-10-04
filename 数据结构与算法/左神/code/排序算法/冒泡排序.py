x = [3,1,9,4,8,6,2,7,10,5]

# 相邻比较大小交换位置，每一次把当前最大值排最后
def _bubble_sort(a):
	if not a or len(a) == 1:
		return a
	# 当前最大值要放入的位置下标
	for i in range(len(a) - 1, 0, -1):
		for j in range(0, i):
			if a[j+1] < a[j]:
				a[j], a[j+1] = a[j+1], a[j]
	return a
	
res = _bubble_sort(x)
print(res)
