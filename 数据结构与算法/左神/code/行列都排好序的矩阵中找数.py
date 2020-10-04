map = [['' for i in range(4)] for i in range(4)]
num=1
for i in range(0,len(map)):	
	for j in range(0,len(map[0])):
		map[i][j]=num
		num+=1
print(map)
def isContains(m,K):
	row = 0
	col = len(m[0])-1
	while row < len(m) and col >= 0:
		if m[row][col] == K:
			return True
		elif m[row][col] < K:
			row += 1
		else:
			col -= 1
	return False
res_0=isContains(map,4)
print(res_0)
res_1=isContains(map,17)
print(res_1)
