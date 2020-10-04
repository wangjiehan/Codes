# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        def get_len(root):
            count = 0
            while root:
                count += 1
                root = root.next
            return count
        len1 = get_len(pHead1)
        len2 = get_len(pHead2)
        if len1 > len2:
            long = pHead1
            short = pHead2
        else:
            long = pHead2
            short = pHead1
        diff = abs(len1 - len2)
        for i in range(diff):
            long = long.next
        while long != short:
            long = long.next
            short = short.next
        return long
