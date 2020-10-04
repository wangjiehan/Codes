import numpy as np


# 统计分词后的词频（按从大到小排序）
def count_element(arr):
    def sort_dic(dic):
        res = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return res
    arr = np.array(arr)
    key = np.unique(arr)
    result = {}
    for k in key:
        mask = (arr == k)
        y_new = arr[mask]
        v = y_new.size
        result[k] = v
    return sort_dic(result)


# list 中元素去重且保持原位置前后关系
def distinct_list(li):
    new_li = list(set(li))
    new_li.sort(key=li.index)
    return new_li


# 对字典按value从大到小排序
def sort_dic(dic):
    ret = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return ret


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 8, 9, 0, 9, 11, 2, 4, 4, 4]
    b = {"a": 1, "b": 3, "c": 2}
    print(count_element(a))
    print(sort_dic(b))
