#直接定义:直接输入
a=[[1,2],[3,4],[5,6]]
print(a)
#数组乘法定义：
b=[['1','2']]*3				#三行两列，三行都是[1,2]
print(b)
#间接定义一个2行3列的二维数组，其中所有元素都是*
c = [['*' for i in range(3)] for i in range(2)]
print(c)
print(len(c),len(c[0]))		#打印二维数组的行、列尺寸
num=1
for i in range(0,len(c)):	#重新初始化二维数组的元素值
	for j in range(0,len(c[0])):
		c[i][j]=num
		num+=1
print(c)
print(c[1][1])			#打印二维数组中第2行第2列元素
'''
以上皆是list格式，若要真正变成数组，需要import numpy
'''
import numpy as np
a = np.array([[1,2],[3,4],[5,6]])
print(a)
