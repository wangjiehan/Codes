'''
11.数值的整数次方
正常解法：
整数次方要分为正数、负数、0三种情况，注意res=1.0，防止把base整型化
python偷懒解法：
base ** exponent
'''
def Power1(base, exponent):
	res = 1.0			#没有int标记的，进行乘除运算或者加了小数点默认为浮点数
	if exponent > 0:
		for i in range(0, exponent):
			res *= base
		return res
	elif exponent < 0:
		for i in range(0, exponent, -1):
			res *= base
		return 1/res
	else:
		return 1
def Power2(base, exponent):
	return base**exponent
if __name__ == '__main__':
	print(Power1(2,3))
	print(Power1(2,-3))	
	print(Power1(2,0))	
	print(Power2(0,2))
