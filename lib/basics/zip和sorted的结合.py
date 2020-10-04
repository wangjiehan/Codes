a = [2, 1 ,3]
b = [4, 2, 6]
c = list(zip(a, b))
print(c)
for i in c:
	print(i)

d = sorted(c, key=lambda x: x[0])
print(d)
