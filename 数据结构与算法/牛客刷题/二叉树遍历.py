# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def threeOrders(self , root ):
        # write code here
#         def first_(root):
#             if not root:
#                 return []
#             left = first_(root.left)
#             mid = [root.val]
#             right = first_(root.right)
#             return mid+left+right
        
#         def mid_(root):
#             if not root:
#                 return []
#             left = mid_(root.left)
#             mid = [root.val]
#             right = mid_(root.right)
#             return left+mid+right
        
#         def last_(root):
#             if not root:
#                 return []
#             left = last_(root.left)
#             mid = [root.val]
#             right = last_(root.right)
#             return left+right+mid
        def first_(root):
            res = []
            stack = [root]
            while stack:
                tmp = stack.pop()
                res.append(tmp.val)
                if tmp.right:
                    stack.append(tmp.right)
                if tmp.left:
                    stack.append(tmp.left)
            return res
        
        def mid_(root):
            res = []
            stack = []
            head = root
            while stack or head:
                if head:
                    stack.append(head)
                    head = head.left
                else:
                    head = stack.pop()
                    res.append(head.val)
                    head = head.right
            return res
        
        def last_(root):
            res = []
            stack = [root]
            while stack:
                tmp = stack.pop()
                res.append(tmp.val)
                if tmp.left:
                    stack.append(tmp.left)
                if tmp.right:
                    stack.append(tmp.right)
            return res[::-1]
        
        return first_(root), mid_(root), last_(root)
