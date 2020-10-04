def sort_dict(dict_):  
	# 排序结果返回二维 list: [[gid1, score1], [gid2, score2] ...]
	def sort_dict_by_value(dic):
		res = sorted(dic.items(), key=lambda x: x[1], reverse=True)
		return res
	# 只按顺序保存 key
	return [i[0] for i in sort_dict_by_value(dict_)]
	
if __name__ == "__main__":
	x = {"a":1, "b": 3, "c": 2}
	print(sort_dict(x))
