'''
小和问题：在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和
求小和，转化为统计当前数 x 的右侧有多少个数比该数大，若有 n 个，则加和 x * n

借用归并排序逻辑，分治左右小和，加起来，再额外加上左右子数组小和
'''

def merge(arr, l, mid, r):
	cnt = 0
	p1, p2 = l, mid + 1
	while p1 <= mid and p2 <= r:
		if arr[p1] < arr[p2]:
			cnt += arr[p1] * (r-p2+1)
			p1 += 1
		else:
			p2 += 1
	return cnt
	
	
def merge_sort(arr, l, r):
	if l == r:
		return 0
	mid = (r + l) // 2
	return merge_sort(arr, l, mid) + merge_sort(arr, mid+1, r) + merge(arr, l, mid, r)
	
if __name__ == '__main__':
	x = [1, 3, 4, 2, 5]
	print(merge_sort(x, 0, len(x) - 1))
