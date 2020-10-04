'''
44.扑克牌的顺子
要求：从扑克牌中随机抽取5张牌，判断是不是顺子，大小王可以当任意值
思路: 使用排序，大小王作为0
（1）先把数组排序
（2）再统计数组中0的个数zeros
（3）最后统计排序后数组中相邻数字之间的空缺总数
	注：如果遇见前后两个数相等，那么直接返回False
（4）比较zeroCount和空缺总数，判断是不是顺子
利用方法arrary.count(n)统计数组中元素为n的个数。
'''
def IsContinuous(numbers):
	if not numbers:
		return False
	numbers.sort()
	zeros = numbers.count(0)
	for i in range(0, len(numbers)-1):
		if numbers[i] != 0:
			if numbers[i] == numbers[i+1]:
				return False
			zeros = zeros - (numbers[i+1] - numbers[i] - 1)
	if zeros < 0:
		return False
	return True
if __name__ == '__main__':
	x = [0,1,3,4,5]
	y = [0,1,4,5,6]
	print(IsContinuous(x))
	print(IsContinuous(y))
