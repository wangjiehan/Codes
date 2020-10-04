'''
50.树中两个结点的最低公共祖先
要求：求普通二叉树中两个结点的最低公共祖先
情况一：如果是二叉搜索树
从根结点开始和两个输入的结点比较：若当前结点的值比两个结点的值都大，那么最低的公共
父结点一定在当前结点的左子树中，当前结点继续向左子结点遍历；若当前结点的值比两个结
点的值都小，那么最低公共父结点一定在当前结点的右子树，当前结点继续向右子结点遍历。
当最终从上到下找到第一个在两个输入结点的值之间的结点，就是最低公共祖先。

情况二：若是普通的树，但有指向父结点的指针
可转换成两个链表的第一个公共结点问题。

情况三：若是普通的树，且没有指向父结点的指针
动态规划
正着来，用两个链表分别保存从根结点到两个输入结点的路径，求两个链表的最后公共结点。
每个输入结点都需要从根结点出发遍历找路径。
两个函数：（1）获取结点路径（递归法）；	（2）输出最后公共结点
'''
class Solution():
	def __init__(self, root, node1, node2):
		self.root = root
		self.node1 = node1
		self.node2 = node2
	def get_path(root, node, path):		#递归法获取结点路径
		if not root or not node:
			return False
		if root == node:
			return True
		path.append(root)
		left = Solution.get_path(root.left, node, path)
		right = Solution.get_path(root.right, node, path)
		if left or right:
			return True
	def get_last_common_node(self):		#输出最后公共结点
		route1 = []
		route2 = []
		res1 = Solution.get_path(self.root, self.node1, route1)
		res2 = Solution.get_path(self.root, self.node2, route2)
		resNode = None
		if res1 and res2:
			length = min(len(route1), len(route2)) 
			index = 0
			while index < length:
				if route1[index] == route2[index]:
					resNode = route1[index]
				index += 1
		return resNode
				
		
		

