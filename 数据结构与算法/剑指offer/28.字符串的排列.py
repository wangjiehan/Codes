'''
28.字符串的排列
例如输入字符串abc,打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
思路：
递归方法：将该问题分解为n个相同的子问题。
两个base case：
（1）字符串为空，返回None；
（2）字符串长度为1，返回字符串。

设str=s1s2...sn;[str] 表示str的全排列，str-sk表示str中去掉第k个字符后的字符串，
则有[str] = [s1[str-s1], s2[str-s2], ...sn[str-sn]];再去求解n个子问题即可。

注意：
（1）不用考虑[str-s1]s1，否则会重复；
（2）排列，为了排除字符相等的情况。当前出现重复字符时，直接continue进入下一步循环。

字符串和数组直接转换的几种方法：（前两者数组的元素都是字符或字符串）
	arr = list(string)是把字符串变成数组，字符串中每个字符对应数组元素
	arr = string.split()是把字符串里每个单词字符串按空格分成数组的元素，存成数组
	str = ''.join(array[…:…])是把数组中字符串格式的元素连接成大的字符串
'''
#输出res是以多条字符串为元素的一维数组['xx','xx','xx'...]

#注意：先用list把字符串变成数组以方便排序排除相等字符的情况，
#再用.join()把数组里的元素连成字符串，变回去
def Permutation(ss):
	if not ss:
		return None
	if len(ss)==1:
		return list(ss)						#注意该条base case写法。后面递归返回什么格式源于此
	res = []
	charlist = list(ss)
	charlist.sort()							#排列，为了排除字符相等的情况
	for i in range(0, len(charlist)):	
		if i >= 1 and charlist[i] == charlist[i-1]:		#注意i >= 1
			continue						#当前出现重复字符时，直接continue不管，进入下一步循环
		tmp = Permutation(''.join(charlist[:i] + charlist[i+1:]))
		for j in tmp:						#tmp里每条元素字符串的开头都加上去掉的那个字符
			res.append(charlist[i] + j)		#字符串相连，并依次添加进入结果res一维数组中
	return res
		
'''
str = "-"
seq = ("a", "b", "c")
print(str.join(seq))
则输出为：a-b-c
'''


'''
字符串的全排列
'''
def all_order_print(strings):
	if len(strings) == 1:
		return [strings]
	res = []
	for i in range(len(strings)):
		res.extend([strings[i]+j for j in all_order_print(strings[:i]+strings[i+1:])]) 
	return res
print(all_order_print('abc'))

