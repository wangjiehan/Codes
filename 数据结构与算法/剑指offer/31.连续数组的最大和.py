'''
31.连续子数组的最大和
输入一个整型数组，数组里有正数也有负数。数组中一个或连续多个整数组成一个子数组。
思路:动态规划问题O(N)
具体判断：f(i)表示以第i个数字结尾的子数组的最大和（必须以当前为结尾），最后返回max[f(i)]。
如果f(i-1) < 0，则f(i) = array[i]; 
如果f(i-1) > 0，则f(i) = f(i-1)+array[i]
在数组从前向后依次遍历，记录每次的“当前结尾下累加最大的子数组和”和“最大子数组和中当前最大值”
'''
def FindGreatestSumOfSubArray(array):
	if not array:					#常规array为空，返回None
		return None
	curSum = 0						# 以当前位置为结尾的子数组的最大和
	greatSum = float('-inf')		# 当前最优结果，初始化为负无穷
	for i in array:
		# 如果以 i - 1 为结尾的子数组的最大和为负数，就直接抛弃之前的结果
		# 因为不管当前第 i 个数是正是负，加上之前的最大和只会使结果变得更小
		if curSum <= 0:			
			curSum = i
		else:
			curSum = curSum + i
		if curSum > greatSum:
			greatSum = curSum
	return greatSum

arr = [1, -2, 3, 10, -4, 7, 2, -5]
print(FindGreatestSumOfSubArray(arr))

