'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        def _get_size(head):
            cnt = 0
            while head:
                cnt += 1
                head = head.next
            return cnt
        if not head:
            return None
        if _get_size(head) < k:
            k = k % _get_size(head)
        if k == 0:
            return head
        first = ListNode(0)
        first.next = head
        slow, fast = first, first
        for _ in range(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        second_line = slow.next
        slow.next = None
        fast.next = first.next
        return second_line
