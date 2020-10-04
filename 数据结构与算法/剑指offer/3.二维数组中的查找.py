'''
3.二维数组中的查找
从右上角开始比较
'''
def arrSearch(m, k):
	r, c = 0, len(m[0])-1
	while r < len(m) and c >= 0:
		if m[r][c] < k:
			r += 1
		elif m[r][c] > k:
			c -= 1
		else:
			return True
	return False
	
	
if __name__ == '__main__':
	map = [['' for i in range(4)] for i in range(4)]
	num = 0
	for i in range(0, 4):
		for j in range(0, 4):
			map[i][j] = num
			num += 1
	print(map)
	print(arrSearch(map, 10))

