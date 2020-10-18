# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def _get_path(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            left = _get_path(root.left) if root.left else []
            right = _get_path(root.right) if root.right else []
            return [[root.val]+token for token in left+right]
        
        path_list = _get_path(root)
        path_list = [int(''.join([str(i) for i in token])) for token in path_list]
        return sum(path_list)
