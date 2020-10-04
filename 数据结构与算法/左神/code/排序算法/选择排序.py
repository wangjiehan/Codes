x = [3,1,9,4,8,6,2,7,10,5]

def _choose_sort(a):
	if not a or len(a) == 1:
		return l
	# i 从 0 至倒数第二个（最小数的下标），每一轮和该一轮第 i 位的数比较大小，把最小的放在i位
	for i in range(0, len(a)-1):
		for j in range(i+1, len(a)):
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
	return a

res = _choose_sort(x)
print(res)
