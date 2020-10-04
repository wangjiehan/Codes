import numpy as np

a=np.random.random()	#随机产生[0,1)范围内的实数
b=int(11*a-5)		#随机产生[-5,5]范围内的整数
print(a)
print(b)

x=[]
c=int(6*a+5)		#随机产生[5,10]范围内的整数，定义为数组长度
print('The length of x is: '+str(c))
for i in range(0,int(c)):
	tmp=np.random.random()
	x.append(int(21*tmp))	#随机产生[0,20]范围内的整数，添加进列表
print(x)

y=x[:]
y.sort()
print(y)	#临时排序，或者用sorted(x)函数
print(x)

d = np.random.randn(5)	#产生标准正态分布的5个随机数
print(d)
