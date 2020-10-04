'''
37.两个链表的第一个公共结点
方法（1）蛮力法：
在第一个链表上顺序遍历每个节点，每遍历到一个节点，就在第二个链表上顺序遍历每个节点，
直到找到第二个链表上有节点和第一个链表上的节点一样停止。（O(mn)）
方法（2）：
如果从两个链表的尾部开始往前比较（后进先出），则最后一个相同结点就是要找的结点，
为此可以借助两个栈，栈顶元素都一样则pop出去，直到找到最后一个相同的元素为止。
（时间复杂度O(m+n),且需要额外辅助空间）
方法（3）：
首先遍历两个链表得到它们的长度，如果m>n，则m链表先走m-n步，然后两个链表再同时走，
直到找到第一个相同的节点（即为它们的第一个公共节点）。
（时间复杂度O(m+n),且不需要额外辅助空间）
'''
class ListNode():
	def __init__(self, x):
		self.val = x
		sef.next = None
def FindFirstCommonNode(pHead1, pHead2):
	len1 = getlength(pHead1)
	len2 = getlength(pHead2)
	if len1 < len2:
		longHead = pHead2
		shortHead = pHead1
	else:
		longHead = pHead1
		shortHead = pHead2
	d = abs(len1 - len2)
	while d > 0:
		longHead = longHead.next
		d -= 1
	while longHead and shortHead and longHead != shortHead:	#三个and条件
		longHead = longHead.next
		shortHead = shortHead.next
	return longHead
def getlength(head):
	count = 0
	while head:
		head = head.next
		count += 1
	return count
		

