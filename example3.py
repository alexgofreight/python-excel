import numpy as np

arr_a = np.array([[1,2],[3,4]])
print(arr_a.sum())
print(arr_a.sum(axis=0))
print(arr_a.sum(axis=1))
print(arr_a.cumsum())
print(arr_a.prod())
print(arr_a.cumprod())