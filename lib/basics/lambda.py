# (1)
add = lambda x, y : x+y
print(add(1,2))  	# 结果为3

# (2)
y1 = lambda x : x**2
print(y1(2))
print((lambda x : x**2)(3))

# (3)
list1 = [3,5,-4,-1,0,-2,-6]
tmp = sorted(list1, key=lambda x: abs(x))
print(tmp)

list1 = [3,5,-4,-1,0,-2,-6]
def get_abs(x):
    return abs(x)
tmp = sorted(list1,key=get_abs)
print(tmp)


