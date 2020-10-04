#1、直接定义：直接输入
a=[1,2,3,4]
print(a)
#2、数组乘法定义：定义一个一维数组，元素都是空
arrSize=int(input('Please enter the size: '))
b=['']*arrSize
print(b)
#3、间接定义：用append方法往空数组中添加元素
c=[]
for i in range(0,arrSize):
	c.append(i+1)
print(c)
#数组元素的交换
c[0],c[1]=c[1],c[0]		#b数组的第一个元素和第二个元素互换
print(c)
