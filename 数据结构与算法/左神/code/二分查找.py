'''
（1）对传入数组排序
（2）初始化left和right
（3）while left <= right的循环条件下（注意=），
	先初始化mid，三种情况更新边界（注意+1、-1）
（4）在while循环外，return mid的其余情况return False
'''
def binary_search(arr, v):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < v:
			left = mid + 1
		elif arr[mid] > v:
			right = mid - 1
		else:
			return mid
	return -1
	
x = [1,3,6,8,9,13,15,18,19,32,45,67,69,80]
print(binary_search(x,18))
print(binary_search(x,32))
print(binary_search(x,11))


# 返回第一个等于v的位置
def binary_search1(arr, v):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < v:
			left = mid + 1
		elif arr[mid] > v:
			right = mid - 1
		else:
			if mid == 0 or arr[mid-1] != v:
				return mid
			else:
				right = mid - 1
	return -1

xx = [1,3,3,6,8]
print(binary_search1(xx, 3))


# 返回最后一个等于v的位置
def binary_search1(arr, v):
	left, right = 0, len(arr) - 1
	while left <= right:
		mid = (left + right) // 2
		if arr[mid] < v:
			left = mid + 1
		elif arr[mid] > v:
			right = mid - 1
		else:
			if mid == len(arr)-1 or arr[mid+1] != v:
				return mid
			else:
				left = mid + 1
	return -1

xxx = [1,3,3,6,8]
print(binary_search1(xxx, 3))
