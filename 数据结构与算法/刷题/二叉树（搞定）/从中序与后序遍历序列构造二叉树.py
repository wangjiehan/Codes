# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    从中序遍历和前序遍历构造是一样的逻辑
    先找根结点
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder and not postorder:
            return None
        head = postorder[-1]
        index = inorder.index(head)

        inorder_left = inorder[:index]
        inorder_right = inorder[index+1:]
        postorder_left = postorder[:index]
        postorder_right = postorder[index:-1]

        head_node = TreeNode(head)
        head_node.left = self.buildTree(inorder_left, postorder_left)
        head_node.right = self.buildTree(inorder_right, postorder_right)
        return head_node
