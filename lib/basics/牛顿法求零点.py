#求f(x)=x**4+x-10的零点
x=float(input('Please enter x0: '))
y=10
while y>0.00000001 or y<-0.00000001:
	y=x**4+x-10
	y_1=4*x**3+1
	x=x-y/y_1
print(x)
