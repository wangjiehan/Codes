'''
42.翻转单词顺序VS左旋转字符串
题目一：翻转单词顺序
要求：翻转一个英文句子中的单词顺序，标点和普通字符一样处理
思路: 
Python中字符串是不可变对象，不能直接用书中的方法（2），但可以转化成列表然后转回去。
	
方法（1）python特性：用split方法把字符串里每个单词按空格分成数组的元素，存成数组
方法（2）两次翻转法：
	第一步翻转句子中所有字符，第二步再翻转每个单词中的字符顺序。
	
字符串和数组直接转换的几种方法：
	string = list(string)是把字符串变成数组，字符串中每个字符对应数组元素
	string = string.split()是把字符串里每个单词按空格分成数组的元素，存成数组
	s = ''.join(array)是把数组中的每个元素变成字符串格式连接成大的字符串
	[str(i) for i in array] 列表解析，变成以字符或者字符串为元素的数组
注意：join()方法要用空格' '连接。之前split去掉了空格。
'''
#方法（1）（推荐）
def ReverseSentence1(s):
	tmp = s.split()			#split()方法把字符串里每个单词按空格分成数组的元素，存成数组
	if len(tmp) == 0:		#s可能全是空格
		return s
	tmp.reverse()
	return ' '.join(tmp[:])	#注意：join()方法要用空格' '连接。之前split去掉了空格
#方法（2）：
'''
转化成列表然后转回去，两个指针pStart和pEnd。
判断pEnd是否走到len(s)-1
判断两个指针位置的元素分别是不是空格' '。
'''
def ReverseSentence2(s):
	if s==None or len(s)<=0:
		return ''
	s=list(s)		#每个字符（包括空格）都变成数组里的元素了
	s=Reverse(s)
	pStart=0
	pEnd=0
	listTmp=[]
	result=''
	while pEnd<len(s):
		if pEnd==len(s)-1:
			listTmp.append(Reverse(s[pStart:]))
			break
		elif s[pStart]==' ':
			pStart +=1
			pEnd +=1
			listTmp.append(' ')
		elif s[pEnd]==' ':
			listTmp.append(Reverse(s[pStart:pEnd]))
			pStart=pEnd
		else:
			pEnd +=1
	for i in listTmp:
		result += ''.join(i)
	return result
def Reverse(s):
	#s是一个list列表
	start=0
	end=len(s)-1
	while(start<end):
		s[start],s[end]=s[end],s[start]
		start+=1
		end-=1
	return s
if __name__ == '__main__':
	s = 'I am a student.'
	print(ReverseSentence2(s))
'''
题目二：左旋转字符串
把字符串前面的若干个字符转移到字符串尾部
方法（1）：利用python特性
方法（2）：三次翻转
比如'abcdefg'要把'ab'移到最后变成'cdefgab'，先根据移动点分成两部分，对两部分分别
调用Revers()翻转，变成'bagfedc'，再对'bagfedc'调用Reverse翻转
'''
#方法（1）（推荐）
def LeftRotateString1(s, n):
	if not s:		
		return ''
	return s[n:]+s[:n]

#方法（2）
def LeftRotateString2(s, n):
	if s is None or len(s)<=0:
		return ''
	if len(s)<=n:
		return s
	s=list(s)
	listTmp=[]
	result=''
	listTmp.append(Reverse(s[:n]))
	listTmp.append(Reverse(s[n:]))
	return ''.join(Reverse(sum(listTemp,[])))
def Reverse(s):
	#s是一个list列表
	start=0
	end=len(s)-1
	while(start<end):
		s[start],s[end]=s[end],s[start]
		start+=1
		end-=1
	return s
#其实方法（2）既然已经数组化了，还不如以下的方法
def LeftRotateString3(s, n):	
	s1 = list(s[0:n])
	s2 = list(s[n:])
	tmp = [s1, s2]
	tmp.reverse()
	res = ''
	for i in tmp:
		res += ''.join(i)
	return res
'''
在python语言里，不论是题目一的（2）还是题目二中的（2）、（3），其实都是多此一举
'''
