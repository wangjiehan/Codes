class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#
# 
# @param head ListNode类 the head node
# @return ListNode类
#
# 先存值，对值排序。再另外根据值构建新的结点，连接出新的链表
class Solution:
    def sortInList(self , head ):
        # write code here
        res = []
        while head:
            res.append(head.val)
            head = head.next
        res_ = sorted(res)
        
        head = ListNode(res_[0])
        tmp = head
        for index in range(0, len(res_)-1):
            next_node = ListNode(res_[index+1])
            head.next = next_node
            head = next_node
        head.next = None
        return tmp
