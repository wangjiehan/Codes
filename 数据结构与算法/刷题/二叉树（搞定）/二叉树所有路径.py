# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def _get_path_list(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [[root.val]]
            left = _get_path_list(root.left) if root.left else []
            right = _get_path_list(root.right) if root.right else []
            return [[root.val]+token for token in left+right]

        def _list2path(arr):
            return ['->'.join([str(i) for i in token]) for token in arr]
        
        path_list = _get_path_list(root)
        return _list2path(path_list)
