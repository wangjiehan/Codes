# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        head = nums[(len(nums)-1)//2]
        left = [token for token in nums if token < head]
        right = [token for token in nums if token > head]
        head_node = TreeNode(head)
        head_node.left = self.sortedArrayToBST(left)
        head_node.right = self.sortedArrayToBST(right)
        return head_node
