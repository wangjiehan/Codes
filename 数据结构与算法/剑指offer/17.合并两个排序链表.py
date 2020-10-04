'''
17.合并两个排序链表
即归并排序中的 merge 环节
根据两个链表结点值的大小关系分情况使用递归，
注意对空链表的单独处理（两个if），即base case
若第11行是def mergeList(self, head1, head2):，则递归时函数名前面要加self.
'''
class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None
def mergeList(head1, head2):
	res = None
	if head1 == None:
		return head2
	if head2 == None:
		return head1
	if head1.val < head2.val:
		res = head1
		res.next = mergeList(head1.next, head2)
	else:
		res = head2
		res.next = mergeList(head1, head2.next)
	return res
