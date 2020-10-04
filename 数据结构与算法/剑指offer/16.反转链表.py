'''
16.反转链表
需要考虑空链表、只有一个结点的链表
'''
class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None
def reverse_link(pHead):
	if pHead == None:
		return None
	pre = pHead
	cur = pHead.next
	pre.next = None
	while cur:
		tmp = cur.next
		cur.next = pre
		pre = cur
		cur = tmp
	return pre
def printList(head):
	a = []
	while head:
		a.append(head.val)
		head = head.next
	return a
if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(4)
	node.next.next = ListNode(7)
	x = reverse_link(node)
	print(printList(x))
