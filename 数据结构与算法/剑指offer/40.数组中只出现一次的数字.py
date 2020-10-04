'''
40.数组中只出现一次的数字
要求：数组中除了两个只出现一次的数字外，其他数字都出现了两遍。
要求时间复杂度O(N)，空间复杂度O(1) （哈希表空间复杂度高）
异或的性质：
（a）如果a、b两个值不相同，则异或结果为1。如果a、b两个值相同，异或结果为0；
	0 ^ 0 = 0
	0 ^ 1 = 1
	1 ^ 0 = 1
	1 ^ 1 = 0
（b）任何数字异或自己都为零。零和任何数异或都等于自己。
思路: 
（1）遍历数组，依次向后按位异或：0先和第一个数异或，得到的结果再和第二个数异或，如此循环。
	即0 ^ arr[0] ^ arr[1] …… ^ arr[-1]
因为异或运算满足交换律，可以证明成对出现的数字全部在异或中抵消了。
所以连续异或最终得到的值，即为那两个只出现一次的数字之间的异或值。
（2）在这个得到的值中找到二进制最后一个1的位置，说明这两个只出现一次的数字在这个位置上是不同的，分别是0和1。
（3）然后把数组里的每个数字按照该位是0还是1分为两组res1和res2，并在各个组中元素连续异或（同（1））。
因为相同的两个数字任意一位都是相同的，所以相同的数字肯定被分在同一个组，异或处理会被抵消。
所以两个数组最终异或的结果分别就是这两个只出现过一次的数字。
'''
def FindNumsAppearOnce(array):
	if len(array) < 2:
		return
	resultEOR = 0
	for i in array:
		resultEOR = resultEOR ^ i
	index = FindFirstBit(resultEOR)
	res1, res2 = 0, 0
	for j in array:
		if IsBit(j, index):
			res1 = res1 ^ j
		else:
			res2 = res2 ^ j
	return [res1, res2]	# 返回值中res1、res2是出现一次的两个数字
def FindFirstBit(num):
	'''
	用于在整数num的二进制表示中找到最右边是1的位
	'''
	indexBit = 0		#从右向左，第一位的位置标记为0
	while num & 1 == 0 and indexBit < 32:
		num = num >> 1	#移位运算，把num转换成二进制后所有位向后移动一位，高位补0
		indexBit += 1	#指针跟上
	return indexBit		#返回最右边第一个是1的位置
def IsBit(num, indexBit):
	'''
	用于判断在num的二进制表示中从右边起的indexBit位是否为1
	'''
	num = num >> indexBit
	return num & 1		#0为False，1为True
x = [2,4,3,6,3,2,5,5]
print(FindNumsAppearOnce(x))

'''
移位运算：
	<< n : 是整体向左移动n位
	>> n : 是整体向右移动n位
'''
