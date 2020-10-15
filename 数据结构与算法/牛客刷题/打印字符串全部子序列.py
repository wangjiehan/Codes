def print_all_sub(string, n, res):
	if n == len(string):						#从前往后的递归
		print(res)
	else:									#两条路同时走
		print_all_sub(string, n+1, res)			#要么此位置不打出来，即空字符
		print_all_sub(string, n+1, res + string[n])	#要么把此位置字符算上
print_all_sub('abc',0,'')						#从0位置开始向后递归，初始res为空

#注意是同时走两条路，要和不要这个字符。如果逻辑是二选一，最终打印只会出现一条结果
#同时走则是计算机自动穷举所有情况

def print_all_sub2(strings):
	if not strings:
		return strings
	res = list(set([strings[0], '']))
	for i in range(1, len(strings)):
		res.extend([token+strings[i] for token in res])
	return res

print(print_all_sub2('abc'))
