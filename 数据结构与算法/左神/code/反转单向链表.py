def rev(link):
	pre = link
	cur = link.next			#存下原链表第一个结点的后指针
	pre.next = None			#设置pre的后指针为空（最后结点）
	while cur:
		tmp = cur.next		#存下当前结点的后指针（先断后）
		cur.next = pre		#让旧链表中的当前结点后指针指向新链表中的pre（再前连）
		pre = cur			#在新链表中把pre前移更新为cur
		cur = tmp			#旧链表中，当前结点后移更新
	return pre
			
#2-4：将原链表的第一个结点变成了新链表的最后一个结点
#6-9：从原链表的第二个结点开始遍历到最后一个结点，将所有结点翻转一遍
