import numpy as np #不as np就每次调用时开头换成numpy.
a=np.array([[1,2],[3,4]])	#array（）将列表数组化
b=np.array([[5,6],[7,8]])
a=np.mat(a)	#mat（）将列表矩阵化
b=np.mat(b)
print(np.shape(a))#矩阵a的规格
print()
print(a+b)	#求矩阵对应位置相加
print()
print(a*b)	#求矩阵相乘
print()
print(np.multiply(a,b)) #求矩阵对应位置相乘
print()
print(a.I)	#求逆矩阵1
print()
print(np.linalg.inv(a))	#求逆矩阵2，还有pinv用于奇异矩阵求逆
print()
print(a.T)	#求转置矩阵
print()
print(np.eye(3))	#输出规格为3的单位矩阵
print()
c=np.arange(0,10,1)	#类似于range（）快速生成数组化的列表
print(c)
print()
c.shape=2,5	#重新规定c的行列大小，重新布局
print(c)
print()
d=c.reshape((5,2))	#将新的行列情况存入新的矩阵，原矩阵c保持不变
print(d)
print(c)
print()
c=np.mat(c)	#必须矩阵化才能矩阵相乘
d=np.mat(d)
print(c*d)
#对于二维数组，需要对元素进行操作时，不要mat转换
