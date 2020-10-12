# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
	'''
	利用非递归版的中序遍历，只不过不缓存，直接每次return，形成一个生成器
	'''
	def __init__(self, root: TreeNode):
		self.head = root
		self.stack = []

	def next(self) -> int:
		"""
		@return the next smallest number
		"""
		while self.stack or self.head:
			if self.head:
				self.stack.append(self.head)
				self.head = self.head.left
			else:
				node = self.stack.pop()
				self.head = node.right
				return node.val

	def hasNext(self) -> bool:
		"""
		@return whether we have a next smallest number
		"""
		if self.stack or self.head:
			return True
		else:
			return False



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
