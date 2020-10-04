import random

'''
先荷兰国旗分好左右,再递归对左右排序
'''

def _gen_arr():
	x = []
	c = random.randint(8, 12)	# 随机产生[8,12]范围内的整数，定义为数组长度
	for i in range(int(c)):
		element = random.randint(0, 10)
		x.append(element)
	return x


def NetherlandsFlag(arr, L, R):			# 对a[L:R]段内切片
	threshold = arr[L+int(len(arr[L:R])*random.random())]
	small_thre, big_thre = L-1, R
	cur = L
	while cur < big_thre:
		# 往小于区域换，若中间无等于区域，则自己和自己换；若有等于区域相当于明确把等于阈值的数换过来，因此指针可以向下
		if arr[cur] < threshold:
			arr[cur], arr[small_thre+1] = arr[small_thre+1], arr[cur]
			small_thre += 1
			cur += 1
		# 往大于区域换，但是换回来的数未知，当前指针需要保持不动，继续比较
		elif arr[cur] > threshold:
			arr[cur], arr[big_thre-1] = arr[big_thre-1], arr[cur]
			big_thre -= 1
		else:
			cur += 1
	return small_thre, big_thre


def quick_sort(arr, L, R):
	if L == R:
		return arr
	small_thre, big_thre = NetherlandsFlag(arr, L, R)
	quick_sort(arr, L, small_thre+1)
	quick_sort(arr, big_thre, R)
	return arr


if __name__ == '__main__':
	x = _gen_arr()
	print(x)
	# x = [3,1,9,4,8,6,2,7,10,5]
	sort_result = quick_sort(x, 0, len(x))
	print(sort_result)

