'''
35.第一个只出现一次的字符
方法（1）：利用python特性，用字符串的两个方法s.count(字符)，
		 直接返回index()就是第一个出现count为1的字符的位置标记。
方法（2）：自定义一个哈希表（字典），键值key为字符，值value为该字符出现的次数。
		  for i in 字典：默认是指key在字典中遍历
		  最后再在s上从头到尾遍历找第一个字典中value为1的字符
'''
def FirstNotRepeatingChar1(s):
	if not s:
		return -1
	for i in s:
		if s.count(i) == 1:
			return i
	return -1
def FirstNotRepeatingChar2(s):
	if not s:
		return -1
	char_dict = {}				#哈希表可以用字典的表示
	for i in s:
		if i in char_dict.keys():
			char_dict[i] += 1
		else:
			char_dict[i] = 1	#如果不在字典里，初始化直接赋值
	for j in s:
		if char_dict[j] == 1:
			return j
	return -1		
if __name__ == '__main__':
	print(FirstNotRepeatingChar1('abaccdeff'))
	print(FirstNotRepeatingChar2('abaccdeff'))
