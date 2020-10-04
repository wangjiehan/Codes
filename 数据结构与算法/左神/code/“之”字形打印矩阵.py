r=int(input('Please enter the Row: '))
c=int(input('Please enter the Column: '))
map = [['' for i in range(c)] for i in range(r)]
num=1
for i in range(0,r):	
	for j in range(0,c):
		map[i][j]=num
		num+=1
print(map)
def printZigZag(m):
	aR=0
	aC=0
	bR=0
	bC=0
	direction = True
	endR=len(m)-1
	endC=len(m[0])-1
	while aR != endR + 1:
		if aC == endC:
			aR += 1
		else:
			aC += 1
		if bR == endR:
			bC += 1
		else:
			bR += 1
		direction = !direction
