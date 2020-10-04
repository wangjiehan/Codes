'''
5.从尾到头打印链表
'''
class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None
#（1）数组逆序（类似于栈）：
def reverseList1(link):
	res = []
	while link:
		res.append(link.val)
		link = link.next
	res.reverse()
	return res
#（2）递归（同理于栈）：
def reverseList2(link):
    if link:
        reverseList2(linke.next)
        print(link.val)
if __name__ == '__main__':
	node1 = ListNode(1)
	node1.next = ListNode(2)
	node1.next.next = ListNode(3)
	print(reverseList1(node1))
