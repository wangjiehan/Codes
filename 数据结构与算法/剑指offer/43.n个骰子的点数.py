'''
43.n个骰子的点数
要求：求出n个骰子朝上一面之和s所有可能值出现的概率
思路：n出现的可能是前面n-1到n-6出现可能的和，设置两个数组，分别保存每一轮

方法（1）：递归（时间效率很低）
把n个骰子分成两堆，第一堆只有一个骰子，第二堆有n-1个骰子，总点数和为第一个骰子的
点数与n-1个骰子的点数和之和。递归结束条件为只剩下一个骰子。
方法（2）：循环（时间效率好）
每新增一个色子，上一轮所有的sum可能都分别加1-6，原sum_list扩展为原来的6倍大小
'''
# 将所有可能的和的列表转为 {和：次数} 的字典
def list2dict(sum_list):
	res = {}
	for key in sum_list:
		if key in res.keys():
			res[key] += 1
		else:
			res[key] = 1
	return res
	

def main(n):
	# 每新增一个色子对上一次sum_list的所有可能的和分别加1-6，对list扩展
	def add_count_single(sum_list):
		res = []
		for x in range(1, 7):
			res.extend([token+x for token in sum_list])
		return res	
	cur = [i for i in range(1, 7)]
	if n < 1:
		return None
	if n == 1:
		return cur
	# 如果 n > 1，从第二个色子开始
	for i in range(1, n):
		cur = add_count_single(cur)
	return cur


def cal_prob(sum_list):
	total = len(sum_list)
	count_dict = list2dict(sum_list)
	return {key: count/total for key, count in count_dict.items()}


if __name__ == '__main__':
	sum_list = main(1)
	print(cal_prob(sum_list))
