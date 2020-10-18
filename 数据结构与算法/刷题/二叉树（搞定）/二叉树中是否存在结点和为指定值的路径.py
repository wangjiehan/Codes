# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @param sum int整型 
# @return bool布尔型
#
class Solution:
    '''
    是否存在
    '''
    def hasPathSum(self , root , sum ):
        # write code here
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        left = self.hasPathSum(root.left, sum-root.val)
        right = self.hasPathSum(root.right, sum-root.val)
        return left or right


class Solution:
    '''
    具体路径
    '''
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        left = self.pathSum(root.left, sum - root.val)
        right = self.pathSum(root.right, sum - root.val)
        return [[root.val]+token for token in left+right]
