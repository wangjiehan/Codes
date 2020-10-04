'''
20.顺时针打印矩阵
考虑矩阵为空的情况
参数：矩阵、圈数标记、矩阵行数、矩阵列数、最终结果
第二个函数中的两条if判断是为了防止单行或单列的情况，当打印半圈后会重复往回打印
'''
def printMatrix(matrix):
	rows = len(matrix) - 1
	cols = len(matrix[0]) - 1
	if not matrix:
		return None
	start = 0			#圈数标记，从0开始
	res = []
	while start * 2 <= rows and start * 2 <= cols:
		print_circle(matrix, start, rows, cols, res)
		start += 1
	return res
def print_circle(matrix, start, rows, cols, res):
	endR = rows - start  	#最后一行标记
	endC = cols - start		#最后一列标记
	for c in range(start, endC+1):
		res.append(matrix[start][c])
	for r in range(start+1, endR+1):
		res.append(matrix[r][endC])
	if start < endR and start < endC:
		for c in range(endC-1, start-1, -1):
			res.append(matrix[endR][c])
	if start < endR and start < endC:
		for r in range(endR-1, start, -1):
			res.append(matrix[r][start])
if __name__ == '__main__':
	arr = [[1]]
	arr2 = [[1,2],
			[3,4]]
	arr3 = [[1,2,3,4,5],
			[6,7,8,9,10],
			[11,12,13,14,15],
			[16,17,18,19,20],
			[21,22,23,24,25]]
	arr4 = [[1],[2],[3],[4]]
	arr5 = [[1,2,3,4,5]]
	print(printMatrix(arr))
	print(printMatrix(arr2))
	print(printMatrix(arr3))
	print(printMatrix(arr4))
	print(printMatrix(arr5))
