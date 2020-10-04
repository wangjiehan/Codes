'''
8.旋转数组的最小数字
使用二分法寻找衔接位置，中间指针数和首位数比较大小，判断衔接点在mid的左边还是右边
但要考虑首位、末位、中间这三个数是同一个值的情况，只能顺序查找
'''
#（1）左右指针法O(logN)或O(N)
def minNumberInRotateArray(rotateArray):
	left = 0
	right = len(rotateArray) - 1
	if rotateArray[int((len(rotateArray)-1)/2)] == rotateArray[0] and rotateArray[0] == rotateArray[-1]:
		return min(rotateArray)                
	while left <= right:		#若直接left<right，mid会始终为left而死循环
		mid = int((right + left)/2)
		if rotateArray[mid] > rotateArray[0]:
			left = mid + 1
		elif rotateArray[mid] < rotateArray[0]:
			right = mid - 1
	return rotateArray[left]
#（2）调用min()函数，O(N)
def minNumberInRotateArray2(rotateArray):
	return min(rotateArray)
if __name__ == '__main__':
	print(minNumberInRotateArray([3,4,5,6,1,2]))
	print(minNumberInRotateArray2([3,4,5,6,1,2]))
