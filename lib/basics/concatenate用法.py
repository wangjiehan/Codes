import numpy as np
a = np.array([[1, 2], [3, 4]]) 
b = np.array([[5, 6]])
print(np.concatenate((a, b), axis=0))  # 这里的axis=0的表示按照行进行合并
'''
array([[1, 2],
       [3, 4],
       [5, 6]])
'''
c = np.array([[1, 2], [3, 4]]) 
d = np.array([[5, 6]])
print(np.concatenate((c, d.T), axis=1))  # 这里的axis=1的表示按照列进行合并
'''
array([[1, 2, 5],
       [3, 4, 6]])
'''
