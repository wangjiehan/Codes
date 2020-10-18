import random

'''
时间复杂度 O(N*log(N))，空间复杂度 O(N)，可以做到 O(1)，但是很难
（1）以列表中点平分列表，
（2）递归对两个列表排序
（3）在对排序好的两个列表merge
'''

def _gen_arr():
	x = []
	c = random.randint(8, 12)	# 随机产生[8,12]范围内的整数，定义为数组长度
	for i in range(int(c)):
		element = random.randint(0, 10)
		x.append(element)
	return x
	

def merge(arr1, arr2):
	res = []
	p1, p2 = 0, 0
	while p1 <= len(arr1) - 1 and p2 <= len(arr2) - 1:
		if arr1[p1] < arr2[p2]:
			res.append(arr1[p1])
			p1 += 1
		else:
			res.append(arr2[p2])
			p2 += 1
	if p1 == len(arr1):
		for i in range(p2, len(arr2)):
			res.append(arr2[i])
	if p2 == len(arr2):
		for i in range(p1, len(arr1)):
			res.append(arr1[i])
	return res
	
def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	mid = len(arr) // 2
	left = arr[:mid]
	right = arr[mid:]
	return merge(merge_sort(left), merge_sort(right))
	
	
if __name__ == '__main__':
	x = _gen_arr()
	print(x)
	# x = [3,1,9,4,8,6,2,7,10,5]
	sort_result = merge_sort(x)
	print(sort_result)
	if sorted(x) == sort_result:
		print('Yes!')
