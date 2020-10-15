def print_all_order(string):
	res = []
	if len(string) == 1:
		return [string]
	for i in range(len(string)):
		res.extend([string[i]+token for token in print_all_order(string[:i]+string[i+1:])])
	return res
print(print_all_order('abc'))
