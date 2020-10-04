'''
4.替换空格
直接使用Python字符串的内置函数replace()
'''
def replaceSpace(s):
	s = s.replace(' ', '%20')
	return s
if __name__ == '__main__':
	txt = 'hello world, hello every day'
	print(txt)
	print(replaceSpace(txt))
'''
一般思路：没替换一个空格，字符串长度增加2，遍历原字符串统计空格个数n，
用原字符串长度加上2n就是新字符串长度
准备两个指针p1、p2，p1指向原字符串末尾，p2指向替换后字符串末尾。
向前移动p1，逐个把指向的字符复制到p2指向的位置，直到碰到第一个空格。
碰到第一个空格，让p1继续向前移动1格，在p2前插入字符串‘20%’，之后p2向前移动3格
