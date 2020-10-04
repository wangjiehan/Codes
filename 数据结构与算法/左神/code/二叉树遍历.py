class Tree():
	def __init__(self, node):
		self.node = node
		self.left = None
		self.right = None
	

def _gen_tree():
	'''
	      1
	  2       3
	4   5   6   7
	'''
	node1 = Tree(1)
	node1.left = Tree(2)
	node1.right = Tree(3)
	node1.left.left = Tree(4)
	node1.left.right = Tree(5)
	node1.right.left = Tree(6)
	node1.right.right = Tree(7)
	return node1
	

tree = _gen_tree()


# 递归法遍历
def _pre_order(tree):
	'''
	先序遍历：中左右
	'''
	if not tree:
		return []
	mid = [tree.node]
	left = _pre_order(tree.left)
	right = _pre_order(tree.right)
	return mid + left + right


def _mid_order(tree):
	'''
	中序遍历：左中右
	'''
	if not tree:
		return []
	left = _mid_order(tree.left)
	mid = [tree.node]
	right = _mid_order(tree.right)
	return left + mid + right


def _post_order(tree):
	'''
	后序遍历：左右中
	'''
	if not tree:
		return []
	left = _post_order(tree.left)
	right = _post_order(tree.right)
	mid = [tree.node]
	return left + right + mid

print("递归法遍历二叉树：")
print("先序遍历", _pre_order(tree))
print("中序遍历", _mid_order(tree))
print("后序遍历", _post_order(tree))


# 非递归法遍历
'''
先序遍历：中左右
利用栈。
（1）根结点作一开始放入。
（2）循环：当栈非空时，弹栈，存下弹栈的结点。
如果弹出的结点的右结点非空，右结点压栈；
接着如果弹出的结点的左结点非空，左结点压栈
'''
print("非递归法遍历二叉树：")

def _pre_order2(tree):
	stack = [tree]
	res = []
	while stack:
		tmp = stack.pop()
		if tmp.right:
			stack.append(tmp.right)
		if tmp.left:
			stack.append(tmp.left)
		res.append(tmp.node)
	return res
print("先序遍历", _pre_order2(tree))


'''
中序遍历：左中右
还是用栈
'''

def _mid_order2(tree):
	stack = []
	head = tree
	res = []
	while stack or head:
		if head:
			stack.append(head)
			head = head.left
		else:
			head = stack.pop()
			res.append(head.node)
			head = head.right
	return res
print("中序遍历", _mid_order2(tree))


'''
后序遍历：左右中
复用先序遍历的逻辑，但是左右压栈的顺序交换，完成中右左顺序
再逆序打印，即左右中
'''
def _post_order2(tree):
	stack = [tree]
	res = []
	while stack:
		tmp = stack.pop()
		if tmp.left:
			stack.append(tmp.left)
		if tmp.right:
			stack.append(tmp.right)
		res.append(tmp.node)
	return res[::-1]
print("后序遍历", _post_order2(tree))


'''
二叉树按层遍历：
用队列
'''
def _layer_order(tree):
	queue = [tree]
	res = []
	while queue:
		tmp = queue.pop(0)
		res.append(tmp.node)
		if tmp.left:
			queue.append(tmp.left)
		if tmp.right:
			queue.append(tmp.right)
	return res
print('按层遍历',  _layer_order(tree)) 

