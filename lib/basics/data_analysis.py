import numpy as np

arr = [1,2,2,3,4,6,8]


# 最小值
def _get_min(arr):
	return min(arr)


# 最大值
def _get_max(arr):
	return max(arr)


# 平均数
def _get_avg(arr):
	return np.mean(arr)


# 中位数
def _get_median(arr):
	return np.median(arr)


# 众数
def _get_mode(arr):
	gm = pd.Series(data=arr)
	return gm.mode()[0]


min_data, max_data = _get_min(arr), _get_max(arr)
avg, median, mode = _get_avg(arr), _get_median(arr), _get_mode(arr)
print(min_data, max_data, avg, median, mode)
