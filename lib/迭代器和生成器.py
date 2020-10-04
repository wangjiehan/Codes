def gen_n_1(arr):
	return iter(arr)
	
def gen_n_2():
	for i in range(5):
		yield i

print('迭代器：')
generator1 = gen_n_1([0, 1, 2, 3, 4])
print(next(generator1))
print(next(generator1))
print('************')
for x in generator1:
	print(x)
	
print('生成器：')
# 生成器就是一个返回迭代器的函数
generator2 = gen_n_2()
print(next(generator2))
print(next(generator2))
print('************')
for x in generator2:
	print(x)
