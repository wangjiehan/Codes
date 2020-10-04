'''
36.数组中的逆序对
数组中左边的数比右边的数大，则这两个数构成一个逆序对。求一个数组中逆序对总数。
借用归并排序，在a[p1] > b[p2]时计数，记录当前b[p2]下，a[p1]之后的每个数都比当前b[p2]要大
（因为更新的是b[p2]）
'''
def merge(a, b):
	p1, p2 = 0, 0
	res = []
	count = 0
	while p1 < len(a) and p2 < len(b):
		if a[p1] <= b[p2]:
			res.append(a[p1])
			p1 += 1
		else:						#在a[p1] > b[p2]时计数
			res.append(b[p2])
			count += len(a[p1:])	#a[p1]之后的每个数都比当前b[p2]要大
			p2 += 1					#因为更新的是b[p2]
	if p1 == len(a):
		for i in range(p2, len(b)):
			res.append(b[i])
	if p2 == len(b):
		for i in range(p1, len(a)):
			res.append(a[i])
	return res, count

def merge_sort(x):
	if len(x) == 1:
		return x, 0
	mid = int(len(x)/2)
	left, count_left = merge_sort(x[:mid])
	right, count_right = merge_sort(x[mid:])
	res, count_merge = merge(left, right)
	return res, count_merge + count_left + count_right	# 左子部分的逆序对数+右子部分的逆序对数+左右联合组对的逆序对数
	
	
if __name__ == '__main__':
	x = [3, 1, 4, 2, 5, 9, 7, 8]
	_, count = merge_sort(x)
	print(count)
