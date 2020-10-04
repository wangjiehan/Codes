# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return bool布尔型
#
class Solution:
    def hasCycle(self , head ):
        # write code here
        slow_cur, fast_cur = head, head
        while fast_cur and fast_cur.next:
            slow_cur = slow_cur.next
            fast_cur = fast_cur.next.next
            if slow_cur == fast_cur:
                return True
        return False
