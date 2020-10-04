def f(x):
	if x<=2:
		return 1
	else:
		return f(x-1)+f(x-2)
x=int(input('Enter x: '))
print(f(x))
