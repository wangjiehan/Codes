def _data(name, *key_list):
	res = []
	for key in key_list:
		res.append([key, name + str(key)])
	return res

print(_data("wjh", 1,2,3,4))
print(_data("wjh", [1,2,3,4]))
print(_data("wjh", *[1,2,3,4]))
print(_data("wjh", *[1,2,3,4], 1))
