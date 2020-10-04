'''
27.二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
思路：
（1）中序遍历，存入数组，
（2）遍历数组，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。
	（此处的left和right指针是指双向链表中的指针）
'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def Convert(pRootOfTree):
	if not pRootOfTree:
		return None
	res = []
	inMidOrder(pRootOfTree)
	for i in range(1, len(res)):	#定义双向链表指针
		res[i-1].right = res[i]
		res[i].left = res[i-1]
	return res[0]
def inMidOrder(root):		#将根结点为root的二叉树中序遍历，添加存到res数组
	if not root:
		return None
	inMidOrder(root.left)	#记住此三行的写法
	res.append(root)
	inMidOrder(root.right)
	
