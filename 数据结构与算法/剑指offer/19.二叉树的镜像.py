'''
19.二叉树的镜像
递归，每个子树上左右结点位置互换
先考虑两种base case情况：
（1）根结点为空
（2）左右子结点都为空
之后：
（1）调换左右结点位置；
（2）递归将左右子树分别做镜像
'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def Mirror(root):
	if not root:
		return
	root.left, root.right = root.right, root.left
	Mirror(root.left)
	Mirror(root.right)
	return root
'''
循环法：若不用递归的方式，用栈
中序遍历后用栈逆序打出来的序列，就是镜像二叉树的中序遍历
或者先序遍历把左和右调换次序
'''
