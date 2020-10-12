class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 
# @param l1 ListNode类 
# @param l2 ListNode类 
# @return ListNode类
#
class Solution:
    def mergeTwoLists(self , l1 , l2 ):
        # write code here
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        tmp = ListNode(0)
        tmp.next = head
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1
                head = head.next
                l1 = l1.next
            else:
                head.next = l2
                head = head.next
                l2 = l2.next
        if not l1:
            while l2:
                head.next = l2
                head = head.next
                l2 = l2.next
        if not l2:
            while l1:
                head.next = l1
                head = head.next
                l1 = l1.next
        return tmp.next
