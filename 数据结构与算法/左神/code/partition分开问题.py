#partition分开问题（不要求排序）：定义0-x指针对应的数的范围为小于等于num区域，
#从x位置处依次向下访问，和num比较，若比num大，则不动继续向下访问，
#若小于等于num，则把这个数和x+1位置（小于等于区域的下一个数）交换，
#相当于扩大小于等于区域。
x=[1,13,4,9,7,8,11,14]
n=8
def partition_array(a,num):
	x=-1		#x指针从-1开始
	for i in range(0,len(a)):
		if a[i]<=num:
			x+=1
			a[x],a[i]=a[i],a[x]
	return a
res=partition_array(x,n)
print(res)
