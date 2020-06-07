import numpy as np

arr = np.arange(27).reshape(3, 3, 3)
print(arr)
arr_copy = arr.copy()
arr = arr.flatten()
print(arr)

#########################################

# remove dimensions, lets say 1 but leave 3 columns

arr_copy = arr_copy.reshape(-1, 3)
print(arr_copy)
