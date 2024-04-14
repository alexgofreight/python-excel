import numpy as np

array_a = np.array([1,2,3,4,5])
print(array_a)

array_b = [1,2,3,4,5]
print(array_b)

arr = np.array([1,2,3,4,5,6])
print(arr.shape)
print(arr.size)

arr = arr.reshape(2, 3)
print(arr)
arr = arr.reshape(3, 2)
print(arr)

arr3 = arr.T
print(arr3)
print(arr3[:, 2])
print('=====')
print(arr3)
print(arr3[0, -1])