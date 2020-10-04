class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 
# @param head ListNode类 
# @param n int整型 
# @return ListNode类
#
class Solution:
    def removeNthFromEnd(self , head , n ):
        # write code here
        tmp = ListNode(0)
        tmp.next = head
        fast_cur, slow_cur = tmp, tmp
        for i in range(n):
            fast_cur = fast_cur.next
        while fast_cur.next:
            fast_cur = fast_cur.next
            slow_cur = slow_cur.next
        slow_cur.next = slow_cur.next.next
        return tmp.next
        
        
                        
                         
                         
                         
                         
                         
