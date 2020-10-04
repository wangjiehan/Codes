#3阶多项式拟合
import numpy as np
x = [1,2,3,4,5,6,7,8,9,10]
y = [2,5,10,22,46,79,80,66,34,78]
n = np.polyfit(x,y,3)		#由高到低多项式前的系数数组
m = np.poly1d(n)			#具体的多项式函数
print(n)
print(m)

