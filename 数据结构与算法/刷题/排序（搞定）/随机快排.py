import random

'''
时间复杂度 O(N*log(N))，空间复杂度 O(log(N))
（1）整个数组荷兰国旗化
（2）国旗左右分治递归排序

若要保持排序稳定性：
在荷兰国旗中建 3 个空的辅助数组，小于、等于、大于的元素依次append进去
但是这样空间复杂度将变为 O(N)
可以做到低空间复杂度情况下保证稳定性，但是很难 01 sort 问题
'''

def _gen_arr():
	x = []
	c = random.randint(8, 12)	# 随机产生[8,12]范围内的整数，定义为数组长度
	for i in range(int(c)):
		element = random.randint(0, 10)
		x.append(element)
	return x


def _flag(arr):
	p1, p2 = -1, len(arr)
	cur = 0
	thre = arr[int((len(arr) - 1) * random.random())]
	while cur < p2:
		if arr[cur] < thre:			# 往小于区域换，若中间无等于区域，则自己和自己换
			arr[cur], arr[p1+1] = arr[p1+1], arr[cur]
			p1 += 1
			cur += 1
		elif arr[cur] > thre:		# 往大于区域换，但是换回来的数未知，当前指针需要保持不动，继续比较
			arr[cur], arr[p2-1] = arr[p2-1], arr[cur]
			p2 -= 1
		else:
			cur += 1
	return arr, p1, p2
	

# 保持稳定性
def _flag2(arr):
	thre = arr[int((len(arr) - 1) * random.random())]
	left, mid, right = [], [], []
	for i in arr:
		if i < thre:
			left.append(i)
		elif i > thre:
			right.append(i)
		else:
			mid.append(i)
	return left+mid+right, len(left)-1, len(left)+len(mid)


def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	arr, p1, p2 = _flag(arr)
	return quick_sort(arr[:p1+1]) + arr[p1+1: p2] + quick_sort(arr[p2:])
	

if __name__ == '__main__':
	x = _gen_arr()
	print(x)
	# x = [3,1,9,4,8,6,2,7,10,5]
	sort_result = quick_sort(x)
	print(sort_result)
	if sorted(x) == sort_result:
		print('Yes!')

