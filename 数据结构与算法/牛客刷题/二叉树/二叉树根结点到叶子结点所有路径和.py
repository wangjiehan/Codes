# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 
# @return int整型
#
class Solution:
    def sumNumbers(self , root ):
        # write code here
        if not root:
            return 0
        def get_str_list(root):
            if not root.left and not root.right:
                return [str(root.val)]
            left = [str(root.val)+token for token in get_str_list(root.left)] if root.left else []
            right = [str(root.val)+token for token in get_str_list(root.right)] if root.right else []
            return left + right
        str_list = get_str_list(root)
        sum_cnt = 0
        for token in str_list:
            sum_cnt += int(token)
        return sum_cnt
