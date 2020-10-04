'''
30.最小的k个数
方法（1）排序，取数组开头0到k-1这k个数，O(NlogN)
方法（2）基于随机快排的partition思路，必须修改输入数组，O(N)
方法（3）基于小根堆，不用修改输入数组（稳定性），O(Nlogk)

注意考虑特殊情况:
	tinput为空 or k超过tinput长度

'''
#方法（2）
'''
基于数组第k个数字来调整（划分数按从小到大排列是第k个），比第k个数字小的放左边，
大的放右边。左边的k个数字就是结果
'''
#方法（3）直接调用python的heapq包里的.nsmallest(n, arr)方法
def GetLeastNumbers(tinput, k):
	import heapq
	if not tinput or k > len(tinput):
		return []
	return heapq.nsmallest(k, tinput)
	#此方法时间复杂度为O(nlogk)
