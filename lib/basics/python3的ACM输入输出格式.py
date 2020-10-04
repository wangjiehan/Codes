'''
自己方法:
输入n行，每一行输入数据，空格分隔（split(',')就是按,分隔）
print(line)：打印每行的一维数组
print(res)：打印所有n行的二维数组
'''
n = int(input())
res = []
for i in range(n):
    line = list(map(int, input().split()))
    res.append(line)
    print(line)
print(res)

'''
牛客网方法：
多行输入，每行对应一个line。
每行字符、字符串输入存于line里，用split()方法从line中转存入数组a中。
每次输入的数据对应数组a中的一个元素。
'''
'''
import sys
count = 0
n = input('Enter n: ')
for line in sys.stdin:
	a = line.split()
	print(int(a[0]) + int(a[1]))
	count += 1
	if int(count) == int(n):
		break
'''

