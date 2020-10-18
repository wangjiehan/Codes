# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.isBalanced(root.left):
            return False
        if not self.isBalanced(root.right):
            return False
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.get_depth(root.left) - self.get_depth(root.right)) > 1:
            return False
        return True
    
    def get_depth(self, root):
        if not root:
            return 0
        return 1 + max(self.get_depth(root.left), self.get_depth(root.right))
