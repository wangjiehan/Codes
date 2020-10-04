'''
26.复杂链表的复制
链表中除了指向后一个结点的指针之外，还有一个指针指向任意结点。
方法（1）：python自带copy包里的deepcopy()方法
方法（2）：复制再拆分，分为三步完成：
（1）复制每个结点，并把新结点放在老结点后面，如1->2,复制为1->1->2->2
（2）为每个新结点设置random指针
（3）把复制后的结点链表拆开
'''
class RandomListNode():
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None
#（1）python自带copy包里的deepcopy()方法
def Clone1(pHead):
	import copy as c
	return c.deepcopy(pHead)
#（2）
def Clone2(pHead):
	if not pHead:
		return None
	CloneNodes(pHead)
	ConnectRandomNodes(pHead)
	return ReconnectNodes(pHead)
def CloneNodes(pHead):
	'''复制原始链表的每个结点，将复制的结点接在其原始结点的后面'''
	pNode = pHead			#这一句很重要，copy下根结点，不在根结点上操作改变！！
	while pNode:
		pCloned = RandomListNode(pNode.label)
		pCloned.next = pNode.next	
		pNode.next = pCloned
		pNode = pNode.next.next
def ConnectRandomNodes(pHead):
	'''将复制后的链表中的克隆结点的random指针链接到被克隆结点random指针指向的结点的的后一个结点'''
	pNode = pHead			#这一句很重要，copy下根结点，不在根结点上操作改变！！
	while pNode:
		pCloned = pNode.next
		if pNode.random:
			pCloned.random = pNode.random.next
		pNode = pNode.next.next
def ReconnectNodes(pHead):
	'''拆分CloneNodes处理后的链表，原始链表的结点组成新的链表，复制结点组成复制后的链表'''
    pNode = pHead
	pClonedHead = pClonedNode = pNode.next	#注意克隆结点的头结点的设置
	pNode.next = pNode.next.next			#pNode设置好头后往下走一步（必须要有）
	pNode = pNode.next
	while pNode:
		pClonedNode.next = pClonedNode.next.next
		pClonedNode = pClonedNode.next
		pNode.next = pNode.next.next
		pNode = pNode.next
	return pClonedHead		#必须返回第一个结点

#（3）递归
def Clone3(pHead):
	if  pHead == None:						#base case
		return None
	newNode = RandomListNode(pHead.label)	#定义结点和值（注意写法）
	newNode.random = pHead.random			#定义random指针
	newNode.next = Clone3(pHead.next)		#定义next指针
	return newNode	
	
#（4）或者用哈希表对应原链表中指针指向和复制链表中的指针指向
