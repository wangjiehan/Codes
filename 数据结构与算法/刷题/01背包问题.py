bag_space = 10
weight = [2, 2, 6, 5, 4]
value = [6, 3, 5, 4, 6]
data = list(zip(weight, value))


# 递归法：
# 当前取物下标为 i 时，朝后取物能做到的背包中物品的最大价值
def bag(data, i, free_w):
	"""
	data: list(zip(weight, value))
	i: 物品下标
	left_w: 背包剩余空间
	
	三种情况：
	（1）候选物品取完(下标走完) or 背包剩余空间为 0 时，背包能装的最大价值返回为 0 (base case)
	（2）当前下标的商品所需空间大于背包中的剩余空间，则返回下一个商品位置的递归
	（3）其余情况（剔除base case、当前物品所需重量超过背包剩余空间），
	    比较添加该物品和不添加该物品后续的最大价值的最大值
	"""
	if i == len(data) or free_w == 0:
		return 0
	if data[i][0] > free_w:
		return bag(data, i+1, free_w)
	else:
		return max(data[i][1]+bag(data, i+1, free_w-data[i][0]), bag(data, i+1, free_w))
		

print(bag(data, 0, bag_space))


# 动态规划法：
def bag_(data, bag_space):
	"""
	可变参数：
	（1）物品下标 i (0至5的整数)
	（2）剩余空间 left_w (0至10的整数)
	
	建一个 6行11列、元素为-1的矩阵 space = [[0]*11 for _ in range(6)]
	根据递归的三种情况，对每个位置赋值：
	（1）最后一行和第一列都是 0
	（2）此外每个位置先判断 i 位的重量和横坐标剩余空间对比：
	    若剩余空间不足，该位的数和下一行的数据相等；
	    若剩余空间足够，该位的数据为下一行数据两种选择的最大值 
	因此要从下往上逆推
	w v	 i\l_w	0	1	2	3	4	5	6	7	8	9	10
	2 6	 0		0	x	x	x	x	x	x	x	x	x	x 
	2 3	 1		0	x	x	x	x	x	x	x	x	x	x 
	6 5	 2		0	x	x	x	x	x	x	x	x	x	x 
	5 4	 3		0	x	x	x	x	x	x	x	x	x	x 
	4 6	 4		0	0	0	0	6	6	6	6	x	x	x 
		 5		0	0	0	0	0	0	0	0	0	0	0 
	"""
	space = [[-1]*(bag_space+1) for _ in range(len(data)+1)]

	for i in range(len(data), -1, -1):
		for j in range(bag_space+1):
			# 第一列和最后一行作为base case 先填好
			if i == len(data) or j == 0:
				space[i][j] = 0
			elif j < data[i][0]:
				space[i][j] = space[i+1][j]
			else:
				space[i][j] = max(data[i][1]+space[i+1][j-data[i][0]], space[i+1][j])
	return space
	
def _find_max_element(arr):
	max_element = []
	for token in arr:
		max_element.append(max(token))
	return max(max_element)


arr = bag_(data, bag_space)
for token in arr:
	print(token)
print(_find_max_element(arr))
