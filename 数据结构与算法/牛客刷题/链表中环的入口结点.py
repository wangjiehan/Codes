# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 
# @param head ListNode类 
# @return ListNode类
#
class Solution:
    def detectCycle(self , head ):
        # write code here
        short_cur, fast_cur = head, head
        while True:
            if fast_cur and fast_cur.next:
                short_cur = short_cur.next
                fast_cur = fast_cur.next.next
                if short_cur == fast_cur:
                    break
            else:
                return None
        fast_cur = head
        while short_cur != fast_cur:
            short_cur = short_cur.next
            fast_cur = fast_cur.next
        return fast_cur
