'''
map()映射的使用方法
'''
arr = ['22','44','66','88']
arr = map(int,arr)
print(list(arr))

# 计算平方数
def square(x) :            
    return x ** 2
a = map(square, [1,2,3,4,5])
print(list(a))
'''
输出：
[1, 4, 9, 16, 25]
'''
# 使用 lambda 匿名函数
b = map(lambda x: x ** 2, [1, 2, 3, 4, 5])
print(list(b)) 
'''
输出：
[1, 4, 9, 16, 25]
'''
 
# 提供了两个列表，对相同位置的列表数据进行相加
c = map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
print(list(c))
'''
输出：
[3, 7, 11, 15, 19]
'''
