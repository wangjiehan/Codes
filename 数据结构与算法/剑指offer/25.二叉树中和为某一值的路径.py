'''
25.二叉树中和为某一值的路径
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
注意:
（1）最终返回的是二维数组，内部每个列表表示找到的路径
（2）考虑为空情况，return []
（3）base case的三个and条件
（4）路径必须走到底
思路：递归（写法记一记）
'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
# 返回二维列表，内部每个列表元素表示满足条件的路径
def FindPath(root, expectNum):
	if not root:
		return []
	# base case
	if root.val == expectNum and root.left == None and root.right == None:
		return [[root.val]]
	# left 和 right 都是二维列表，每个元素为满足条件的路径
	left = FindPath(root.left, expectNum - root.val)
	right = FindPath(root.right, expectNum - root.val)
	return [[root.val] + token for token in left+right]
'''
两个数组直接相加 = 两个数组内元素相连成一个数组
如print([1]+[2])，对应输出为[1, 2]
再如print([[1,2],[3,4]] + [[5,6]])，对应输出为[[1,2],[3,4],[5,6]]
以上的left + right，left和right都是和res一样的二维数组（递归一致性），
left和right相加则是把所有除了root结点外的路径作为二维数组的行相连合并起来，
i则对应相连合并后的二维数组中的每一行（即每条除了root结点外的路径）
'''
