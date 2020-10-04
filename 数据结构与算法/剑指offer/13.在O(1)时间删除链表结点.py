'''
13.在O(1)时间删除链表结点
如果有后续结点，后续结点的值前移，删除后续结点；如果没有，就只能顺序查找了
把删除当前结点转为删除当前结点的后续结点，就不用知道当前删除结点的前一个结点
先讨论两种特殊情况：
（1）link里面只有一个结点，就是要和删除的结点，则让link为空；
（2）要删除的结点在最后一位，则只能遍历到倒数第二位结点，并让其next指针指向None。
'''
class ListNode():
	def __init__(self, x):
		self.val = x
		self.next = None
def deleteNode(link, del_node):
	if link == del_node:		#如果只有一个结点
		link = None
	if del_node.next == None:	#如果要删除的结点在末尾，顺序遍历到最后
		while link.next.next:
			link = link.next
		link.next = None					
	del_node.val = del_node.next.val	#如果要删除的结点有后续结点
	del_node.next = del_node.next.next	
if __name__ == '__main__':
	node1 = ListNode(1)
	node1.next = ListNode(2)
	node1.next.next = ListNode(3)
	deleteNode(node1, node1.next)
	print(node1.val,node1.next.val)
'''
表示该值是一个空对象，空值是Python里一个特殊的值，用None表示。
None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
可以将None赋值给任何变量，也可以给None值变量赋值
'''
