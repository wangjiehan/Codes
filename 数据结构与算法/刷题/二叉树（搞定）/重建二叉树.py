# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	'''
	输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
	'''
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		if not preorder and not inorder:
			return None
		head = TreeNode(preorder[0])    
		i = inorder.index(preorder[0])
		inorder_left = inorder[:i]
		inorder_right = inorder[i+1:]
		preorder_left = preorder[1:i+1]
		preorder_right = preorder[i+1:]
		head.left = self.buildTree(preorder_left, inorder_left)
		head.right = self.buildTree(preorder_right, inorder_right)
		return head
