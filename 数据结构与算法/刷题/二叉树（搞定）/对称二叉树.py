# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	'''
	给定一个二叉树，检查它是否是镜像对称的。
	例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
	'''
	def isSymmetric(self, root: TreeNode) -> bool:
		def _mid_left(root):
			if not root:
				return ['#']
			left = _mid_left(root.left)
			mid = [root.val]
			right = _mid_left(root.right)
			return mid+left+right

		def _mid_right(root):
			if not root:
				return ['#']
			left = _mid_right(root.left)
			mid = [root.val]
			right = _mid_right(root.right)
			return mid+right+left
		
		return _mid_left(root) == _mid_right(root)
