'''
49.把字符串转换成整数
要求：把字符串转化成整数
测试用例：正负数和0，空字符，包含其他字符
备注：使用raise抛出异常作为非法提示
方法（1）直接调用python库函数int（新结构： try:……	except:……）
方法（2）把合法输入的集合列出来，并考虑开头+、-符号，非法输入时直接返回0
	调用ord()方法，通过和字符串'0'序号的差值，将字符格式变成整型
'''
#方法（1）
def StrToInt1(s):
	try:
		return int(s)
	except:
		return 0
#方法（2）
def StrToInt2(s):
	numstrs = ['0','1','2','3','4','5','6','7','8','9']
	sum = '0'
	sign = 1
	for i in range(0, len(s)):
		if i == 0:
			if s[i] == '-':		#开头是+、-时额外讨论
				sign = -1
				continue		#continue跳过剩余代码，直接进入下一步循环s[1]
			elif s[i] == '+':
				continue
		if s[i] not in numstrs:
			return 0	
		sum = sum + s[i]		#用python里字符串相连再int化是最方便的
	return int(sum) * sign
if __name__ == '__main__':
	print(StrToInt1('1a234'))
	print(StrToInt1('1234'))
	print(StrToInt2('1a234'))
	print(StrToInt2('1234'))	
			
