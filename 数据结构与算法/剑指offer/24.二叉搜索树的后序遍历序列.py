'''
24.二叉搜索树的后序遍历系列：判断给定的整数数组是不是二叉搜索树的后序遍历序列
二叉搜索树定义：中序遍历依次升序的二叉树
整数数组中不包含重复值
思路：递归
（1）考虑序列为空时，直接返回False
（2）整数序列的最后一个数是根结点。
（3）找到左右子树划分点。二叉搜索树中，比根结点小的值都在左子树里，剩下的是右子树。
（4）如果划分点右边至倒数第二个数中，存在小于根结点的数，则返回False
（5）递归左右子树。注意递归的base case的两种条件。
'''
def VerifySquenceOfBST(sequence):
	if not sequence:
		return False
	root = sequence[-1]
	p = -1
	for node in sequence[:-1]:
		if node >= root:
			break
		else:
			p += 1			#p表示左子树的下标范围，左子树标记是从0到p
	for node in sequence[p:-1]:
		if node < root:
			return False
	if p == -1 or p == len(sequence) - 2:	# 注意此base case表达，表示没有左子树或者没有右子树时，直接return True
		return True
	left = VerifySquenceOfBST(sequence[:p])
	right = VerifySquenceOfBST(sequence[p:len(sequence)-1])
	return left and right
print(VerifySquenceOfBST([4,6,7,5]))
