'''
23.从上往下打印二叉树
按层遍历：（和图的广度优先遍历一样）：
借助队列，从根结点开始，进入队列，出队打印的同时让该结点的左右两个子结点按顺序进入队列。
之后每次一个数出队列，当队列不为空时都循环以上操作。
出队打印的数依次进入额外申请的res数组中。
'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def PrintFromTopToBottom(root):
	if not root:
		return None
	queue = [root]
	res = []
	while queue:
		node = queue.pop(0)
		res.append(node.val)
		if node.left:			#先进左，后进右
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	return res
