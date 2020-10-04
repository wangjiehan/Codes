import random

'''
时间复杂度 O(N*log(N))，空间复杂度 O(1)
堆排序：
（1）先把原数组变成大根堆_heap_insert
（2）再把根结点（最大值）和最后一个数交换，则一个小的值跑到了根结点
（3）把根结点为小值进行下沉，使原完全二叉树恢复大根堆形式
这样可以避免使用递归
'''

def _gen_arr():
	x = []
	c = random.randint(8, 12)	# 随机产生[8,12]范围内的整数，定义为数组长度
	for i in range(int(c)):
		element = random.randint(0, 10)
		x.append(element)
	return x


# 新插入的结点下标为 i 时，把该结点向上插入使 arr 为大根堆
def _heap_insert(arr, index):
	while arr[index] > arr[int((index-1)/2)]:
		arr[index], arr[int((index-1)/2)] = arr[int((index-1)/2)], arr[index]
		index = int((index-1)/2)


# 若小数值结点的下标为 index，将该值下沉，数组重新调整为大根堆
def _heapify(arr, index, heap_thre):
	left = index * 2 + 1
	while left <= heap_thre:
		# 左右子结点先比出来谁最大，再和父结点比较
		if left+1 <= heap_thre and arr[left+1] > arr[left]:
			largest = left+1
		else:
			largest = left
		if arr[largest] > arr[index]:
			arr[index], arr[largest] = arr[largest], arr[index]
		index = largest
		left = index * 2 + 1


def _heap_sort(arr):
	if len(arr) <= 1:
		return arr
	for i in range(len(arr)):
		_heap_insert(arr, i)
	heap_thre = len(arr) - 1
	while heap_thre > 0:
		arr[0], arr[heap_thre] = arr[heap_thre], arr[0]
		heap_thre -= 1
		_heapify(arr, 0, heap_thre)
	return arr


if __name__ == '__main__':
	x = _gen_arr()
	print(x)
	# x = [3,1,9,4,8,6,2,7,10,5]
	sort_result = _heap_sort(x)
	print(sort_result)
	if sorted(x) == sort_result:
		print('Yes!')

