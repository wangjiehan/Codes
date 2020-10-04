'''
18.树的子结构，即判断一棵二叉树pRoot2是不是另一个pRoot1的子结构
使用递归

第一步，查找pRoot1中和pRoot2中根结点值一样的结点：
（1）pRoot1和pRoot2都非空时要判断是否两个.val相等，若发现有，则进入第二步判断子结构是否相同；
（2）最终结果的判断同时也要根据第二步判断的结果，若False则继续向pRoot1的左或右子树递归此函数判断。

第二步，判断pRoot1中以某个结点为根结点的子树是不是和pRoot2有相同的结构：
（1）pRoot2走到空时则可返回True；（（1）和（2）if的判断次序不可改）
（2）pRoot1走到空时必然返回False；
	（因为先判断（1），若同时走到空仍会返回True，返回False说明没有进入（1）而先走完了pRoot1）
（3）pRoot1和pRoot2的.val不同时必然返回False
以上三个为base case，pRoot1和pRoot2分别同时向左and向右递归此函数（左右必须同时为True才能返回True）

# 最简单的方法：
（1）两棵树分别做先或中或后序遍历，转成字符串（包含值和内存），结点中间加连接符
（2）判断子结构遍历的字符串是否in大结构遍历的字符串中
'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def HasSubtree(pRoot1, pRoot2):		#两个if， ==， or
	if pRoot2 == None:		#俩base case，一共4个if
		return True
	if pRoot1 == None:
		return False
	#非base case部分：
	if pRoot1 == pRoot2:
		return is_same_tree(pRoot1, pRoot2)
	else:
		return HasSubtree(pRoot1.left,pRoot2) or HasSubtree(pRoot1.right,pRoot2)
	
	
def is_same_tree(pRoot1, pRoot2):	#判断pRoot2结点下的结构和pRoot1下的结构是否一样
	if not pRoot1 and not pRoot2:
		return True
	#非base case部分：
	if pRoot1 != pRoot2:
		return False
	return is_same_tree(pRoot1.left,pRoot2.left) and is_same_tree(pRoot1.right,pRoot2.right)
