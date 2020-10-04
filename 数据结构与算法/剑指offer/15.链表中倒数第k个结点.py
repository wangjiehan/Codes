'''
15.链表中倒数第k个结点
使用快慢指针，快的先走k-1步（若从头结点开始，则是走k-2步）
快指针来到第k个结点时，慢指针同时进入第1个结点。
需要考虑空链表、k小于等于0以及k小于等于链表长度（快指针走到k及其之前就走完整个链表了）
'''
class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None
def last_kth(link, k):
	pBehind = None
	pAhead = link
	if link == None or k <=0:	#空链表、k小于等于0
		return None
	for i in range(1, k-1):		#初始定义pAhead从link开始，已经算走了一步了，只需再走k-2步
		if pAhead.next == None:			#k小于等于链表长度的情况
			return None
		pAhead = pAhead.next
	pBehind = link
	pAhead = pAhead.next
	while pAhead.next:
		pAhead = pAhead.next
		pBehind = pBehind.next
	return pBehind.val
if __name__ == '__main__':
	node = ListNode(1)
	node.next = ListNode(4)
	node.next.next = ListNode(7)
	print(last_kth(node, 2))
