'''
41.和为s的两个数字VS和为s的连续正数序列
题目一：和为s的两个数字：O(N)
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
思路: 设置头尾两个指针，若和大于s，尾指针减小（向左），否则头指针增加（向右）
'''
def FindNumbersWithSum(array, s):
	pHead, pEnd = 0, len(array) - 1
	while pHead < pEnd:		
		if array[pHead] + array[pEnd] < s:
			pHead += 1
		elif array[pHead] + array[pEnd] > s:
			pEnd -= 1
		else:
			return [array[pHead], array[pEnd]]
	return None
'''
题目二：和为s的连续正数序列
输入一个正数s， 打印出所有和为s的正整数序列（至少两个数）
思路: 使用两个指针，和比s小，大指针后移，比s大，小指针后移
初始化左右指针数为1和2。因为至少要有两个数，while循环在small < (s+1)/2 时。
利用求和函数sum(range(a, b))：a到b-1范围求和
'''
def FindContinuousSequence(s):	
	small, big = 1, 2
	res = []
	while small < int(s/2+1):
		if sum(range(small, big + 1))  < s:
			big += 1
		elif sum(range(small, big + 1))  > s:
			small += 1
		else:
			res.append(list(range(small, big + 1)))	#把一组结果list化添加进最终结果数组
			small += 1				#继续向后找（继续把后面找到的结果添加，则形成二维数组）
	return res
if __name__ == '__main__':
	x = [1,2,4,7,11,15]
	print(FindNumbersWithSum(x, 15))
	print(FindContinuousSequence(9))
	
	
