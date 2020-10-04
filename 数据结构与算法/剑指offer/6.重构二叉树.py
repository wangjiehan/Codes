'''
6.重构二叉树
通过先序遍历确定根结点位置，再在中序遍历中找出根结点位置，
通过中序遍历确定根结点的左右子树尺寸
在先序遍历中找到左右子树范围
对左右子树递归
'''
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
# 返回构造的TreeNode根节点
def reConstructBinaryTree(pre, tin):
	if len(pre) == 0 or len(tin) == 0:
		return None
	for i in range(0, len(tin)):		#在中序遍历中记录下根结点位置
		if tin[i] == pre[0]:
			break
	root = TreeNode(pre[0])
	root.left = reConstructBinaryTree(pre[1:i+1],tin[:i])
	root.right = reConstructBinaryTree(pre[i+1:],tin[i+1:])
	return root
