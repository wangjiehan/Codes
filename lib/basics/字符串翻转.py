str = 'abc'
def ReverseStr(s):
	return s[::-1]
print(ReverseStr(str))

def reversStr(string):
	tmp = ''
	for i in range(len(string)):
		tmp += string[len(string)-i-1]
	return tmp
print(reversStr(string))
