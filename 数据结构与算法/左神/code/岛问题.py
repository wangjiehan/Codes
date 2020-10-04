m1 = [  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
		[ 0, 1, 1, 1, 0, 1, 1, 1, 0 ], 
		[ 0, 1, 1, 1, 0, 0, 0, 1, 0 ],
		[ 0, 1, 1, 0, 0, 0, 0, 0, 0 ], 
		[ 0, 0, 0, 0, 0, 1, 1, 0, 0 ], 
		[ 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],]
def countIsland(m):
	if len(m) == 0 or len(m[0]) == 0:
		return 0
	r = len(m)
	c = len(m[0])
	countnum = 0			
	for i in range(0, r):
		for j in range(0, c):
			if m[i][j] == 1:
				countnum += 1		#计数
				infect(m,i,j,r,c)	#遇到1就感染
	return countnum
def infect(m,i,j,r,c):
	if i < 0 or i >= r or j < 0 or j>= c or m[i][j] != 1:
		return						#直接return,相当于什么都没做
	m[i][j] = 2
	infect(m,i+1,j,r,c)				#四个邻近位置递归调用
	infect(m,i-1,j,r,c)
	infect(m,i,j+1,r,c)
	infect(m,i,j-1,r,c)
res=countIsland(m1)
print(res)
				        
