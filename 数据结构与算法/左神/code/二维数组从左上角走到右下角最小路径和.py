map = [['' for i in range(4)] for i in range(4)]
num=1
for i in range(0,len(map)):	
	for j in range(0,len(map[0])):
		map[i][j]=num
		num+=1
print(map)
def countlen(m,i,j):
	if i == len(m)-1 and j == len(m[0])-1:
		return m[i][j]
	if i == len(m)-1:
		return m[i][j] + countlen(m,i,j+1)
	if j == len(m[0])-1:
		return m[i][j] + countlen(m,i+1,j)
	right = countlen(m,i,j+1)			#右边位置到右下角的最短路径和
	down = countlen(m,i+1,j)			#下边位置到右下角的最短路径和
	return m[i][j] + min(right,down)	#选择后一步（向右或向下）情况下最短路径
print(countlen(map,0,0))
#第9-14都相当于base case（终止条件）

#重复过程太多，一个结点处的最小路径和被上一个和左一个都算过
#用动态规划存到缓存中，不用重复计算
