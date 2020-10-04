arr = [ [1, 2, 3], 
		[4, 5, 6],
		[7, 8, 9]]

def _go_edge(arr, r0, c0, r1, c1):
	n = 0
	for i in range(c0, c1):
		arr[r0][i], arr[r0+n][c1] = arr[r0+n][c1], arr[r0][i]
		arr[r1][c1-n], arr[r0][i] = arr[r0][i], arr[r1][c1-n]
		arr[r1-i][c0], arr[r0][i] = arr[r0][i], arr[r1-i][c0]
		n += 1
		
for i in range(int((len(arr)+1)/2)):
	if i <= len(arr)-1-i and i <= len(arr[0])-1-i:
		_go_edge(arr, i, i, len(arr)-1-i, len(arr[0])-1-i)
print(arr)
