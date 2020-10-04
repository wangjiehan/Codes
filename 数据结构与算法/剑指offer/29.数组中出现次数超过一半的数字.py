'''
29.数组中出现次数超过一半的数字
方法（1）暴力排序，中位数即为次数超过一半的数字
方法（2）基于堆排序（一个大根堆，一个小根堆）在O(N)下找中位数，必须修改次序
方法（3）遍历数组时保存两个值：数组中的一个数字、次数
当遍历到下一个数时，若下一个数和之前保存的数字相同，则次数加1,；若不同，则次数减1；
若次数为0，需要保存下一个数，把次数设为1。要找的数的次数比其他所有数次数之和还要高，
所以要找的数如果存在，则肯定是遍历结束后最后存下的数。
但是最后要判断一下这个数出现的次数是不是超过一半，有可能根据元素分布的特殊性，不存在
这样的中位数，即次数小于一半。若不存在这样的数，返回0
'''
def MoreThanHalfNum(numbers):
	if not numbers:
		return 0
	res = numbers[0]
	count = 1
	for i in range(0, len(numbers)):
		#每次循环要先判断一下count是不是为0
		if numbers[i] == res:
			count += 1
		else:
			count -= 1
		if count == 0:		
			res = numbers[i]
			count = 1
	'''最后判断一下，有可能元素分布有特殊性。
	   若结果res的次数小于数组长度的一半，即不存在，返回0'''
	count2 = numbers.count(res)
	if count2 <= int(len(numbers)/2):	#注意 <=
		return 0
	return res
