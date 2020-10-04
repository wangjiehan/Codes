# 递归
def f(x):
	if x<=2:
		return 1
	else:
		return f(x-1)+f(x-2)
x=int(input('Enter x: '))
print(f(x))

# 动态规划
a=[1,1]
n = int(input("Please enter n: "))
for i in range(2, n):
	tmp = a[i-1] + a[i-2]
	a.append(tmp)
print(a[n-1])
