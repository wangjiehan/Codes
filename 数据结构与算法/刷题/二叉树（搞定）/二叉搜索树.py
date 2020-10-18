# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	'''
	给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
	'''
	def generateTrees(self, n: int) -> List[TreeNode]:
		if not n:
			return None
		n_list = range(1, n+1)
		def _gen_tree(n_list):
			res = []
			if len(n_list) == 0:
				return [None]
			if len(n_list) == 1:
				return [TreeNode(n_list[0])]
			for i in range(len(n_list)):
				for left in _gen_tree(n_list[:i]):
					for right in _gen_tree(n_list[i+1:]):
						head = TreeNode(n_list[i])
						head.left = left
						head.right = right
						res.append(head)
			return res
		return _gen_tree(n_list)
