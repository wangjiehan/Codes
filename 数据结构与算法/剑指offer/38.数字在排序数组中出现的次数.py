'''
38.数字在排序数组中出现的次数
使用二分法分别递归找到数组中第一个和最后一个出现的值的坐标，然后相减
O(logN)（即使递归次数可能很大，但在二分法里面进行，默认递归的复杂度约为二分法复杂度）
若直接二分查找找到该数后向前向后同时遍历，则时间复杂度为O(N)

分getFirst和getLast两个函数，都是基于二分法。
'''
def GetNumberOfK(data, k):
	first = getFirst(data, k)
	last = getLast(data, k)
	#考虑当first和last都为None时（只可能同时为None、同时不为None）因为为空说明没有这个数
	if first == None and last == None:	
		return 0
	return last - first + 1
	
	
def getFirst(arr, k):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = int((right - left)/2 +left)
		if arr[mid] < k:
			left = mid + 1
		elif arr[mid] > k:
			right = mid - 1
		else:
			if mid - 1 >= 0 and arr[mid-1] == k:	#注意条件
				right = mid - 1			#挪一下右边界，继续二分法
			else:				#不要忘了else!!!前面的if里没有return
				return mid 
	return None
	
	
def getLast(arr, k):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = int((right - left)/2 +left)
		if arr[mid] < k:
			left = mid + 1
		elif arr[mid] > k:
			right = mid - 1
		else:
			if mid + 1 <= len(arr) - 1 and arr[mid+1] == k:
				left = mid + 1			#挪一下左边界，继续二分法
			else:
				return mid
	return None
if __name__ == '__main__':
	x = [1, 2, 3, 3, 3, 3, 5, 6]
	x2 = [1, 2, 3, 3, 3]
	print(GetNumberOfK(x, 3))
	print(GetNumberOfK(x, 4))
	print(GetNumberOfK(x2, 3))
