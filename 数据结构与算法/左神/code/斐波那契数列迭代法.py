a=[1,1]
n = int(input("Please enter n: "))
for i in range(2, n):
	tmp = a[i-1] + a[i-2]
	a.append(tmp)
print(a[n-1])
