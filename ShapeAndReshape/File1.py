import numpy as np

a = np.array([1, 2, 3])

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], ])

# data type

# print(a.dtype)
# print(b.dtype)

# size
# print(b.itemsize)
# print(a.nbytes)

array = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(array.shape)

# get specfic element  [r,c]
# say we want 13, it's the second row and 5th column...
# index starts 0

print(array[1, 5])
print(array[0, :])  # get specific row ie 1st row and all columns

# get specific column
print(array[:, 2])  # all the rows and 2nd column
