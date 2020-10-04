'''
14.调整数组顺序使奇数位于偶数前面
其实就是荷兰国旗问题
使用两个指针，前后各一个，
左指针遇到奇数，循环向后；右指针遇到偶数，循环向前。如果遇到左偶数、右奇数，则交换
用和1的与运算（&）是否等于1判断是否为奇数
为了更好的扩展性，可以把判断奇偶函数部分抽取出来，以方便今后修改处理同类问题
'''
def reorder(arr, function):		#注意function后面不用加()，只传递函数名
	left,right = 0,len(arr)-1
	while left < right:			#while套两个while，内部也可以套用三个同时进行的if
		while function(arr[left]):
			left += 1
		while not function(arr[right]):
			right -= 1
		if function(arr[left]) is False and function(arr[right]) is True:
		#此行的if语句其实可以省略，因为以上两个while遇到左偶右奇会自动跳出
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1 
	return arr
def is_odd(num):
	return (num % 2) == 1	#位与运算。或者用%2除以2的余数来判断。


# 荷兰国旗法
def reorder2(arr):
	p1, p2 = -1, len(arr)
	cur = 0
	while cur < p2:
		if is_odd(arr[cur]):
			arr[cur], arr[p1+1] = arr[p1+1], arr[cur]
			cur += 1
			p1 += 1
		else:
			arr[cur], arr[p2-1] = arr[p2-1], arr[cur]
			p2 -= 1
	return arr


if __name__ == '__main__':
	x = [1,2,4,5,6,7,8,9,11,10]
	print(reorder(x, is_odd))	#注意function后面不要加()了，否则提示没有num传入
	print(reorder2(x))


