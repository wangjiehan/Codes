arr = [ [1, 2], 
		[4, 5], 
		[7, 8],
		[10,11]]

def _go_edge(arr, r0, c0, r1, c1):
	res = []
	if r0 == r1:
		for i in range(c0, c1+1):
			res.append(arr[r0][i])
	elif c0 == c1:
		for i in range(r0, r1+1):
			res.append(arr[i][c0])
	else:
		for i in range(c0, c1):
			res.append(arr[r0][i])
		for i in range(r0, r1):
			res.append(arr[i][c1])
		for i in range(c1, c0, -1):
			res.append(arr[r1][i])
		for i in range(r1, r0, -1):
			res.append(arr[i][c0])
	return res

res = []
for i in range(int((len(arr)+1)/2)):
	if i <= len(matrix)-1-i and i <= len(matrix[0])-1-i:
		res.extend(_go_edge(arr, i, i, len(arr)-1-i, len(arr[0])-1-i))
print(res)
