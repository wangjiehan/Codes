import numpy as np
a = np.array([1,2,3])
b = np.array([2,5,13])
x = np.vstack((a,b))
print(x)
print(np.corrcoef(a, b))
print(np.corrcoef(x))
print(np.corrcoef(x)[0, 1])
