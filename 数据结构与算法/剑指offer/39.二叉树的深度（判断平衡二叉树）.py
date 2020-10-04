'''
39.二叉树的深度
思路：递归实现
（1）如果一棵树结点为空，返回深度为0
（2）其余情况，数的深度是左子树和右子树深度较大者加1
'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def TreeDepth(pRoot):
	if not pRoot:
		return 0
	return max(TreeDepth(pRoot.right), TreeDepth(pRoot.left)) + 1
'''
拓展：是否为平衡二叉树
非平衡二叉树的三种情况：
（1）左子树不是平衡二叉树
（2）右子树不是平衡二叉树
（3）左右子树都是平衡二叉树时，左右子树深度差的绝对值大于1
除了以上三种情况，其余的情况都是平衡二叉树
注意：
	base case里pRoot为空时返回True
'''
def IsBalanced(pRoot):
	if not pRoot:		# 1 + 3
		return True
	if not IsBalanced(pRoot.left):
		return False
	if not IsBalanced(pRoot.right):
		return False
	if IsBalanced(pRoot.left) and IsBalanced(pRoot.right) and abs(TreeDepth(pRoot.left) - TreeDepth(pRoot.right)) > 1:
		return False
	return True
def TreeDepth(pRoot):
	if not pRoot:
		return 0
	return 1 + max(TreeDepth(pRoot.right), TreeDepth(pRoot.left))
	
