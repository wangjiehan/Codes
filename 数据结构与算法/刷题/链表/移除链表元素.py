'''
删除链表中等于给定值 val 的所有节点。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        def _get_list(head, val):
            res = []
            while head:
                if head.val != val:
                    res.append(head.val)
                head = head.next
            return res
        val_list = _get_list(head, val)

        def _gen_node(val_list):
            tmp = ListNode(0)
            head = ListNode(val_list[0])
            tmp.next = head
            for i in range(1, len(val_list)):
                node = ListNode(val_list[i])
                head.next = node
                head = head.next
            head.next = None
            return tmp.next
        
        return _gen_node(val_list) if val_list else None
