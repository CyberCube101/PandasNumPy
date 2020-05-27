import numpy as np

# numpy is computationally faster than lists!
# Data must be same type!
# numpy integers rely on C-type integers, whereas python has unlimited integer range

# x = np.arange(1000)

y = np.arange(10000)
y = y ** 2

# in a list we need to write more code

z = list(range(10000))
squared = [x ** 2 for x in z]

print(y.sum(dtype=np.int64))  # specify 64 bit to stop overflow
print(sum(squared))
##################################################################
# 32 bit range
bit_32 = 2 ** 32 - 1
# Therefore max value is half of this
max_32 = bit_32 / 2

# 64 bit range
bit_64 = 2 ** 64 - 1
max_64 = bit_64 / 2

#################################################################

ndim = np.arange(27)
print(ndim)
# now lets make it a 3x3x3
ndim = np.arange(27).reshape(3, 3, 3)
print(ndim)

##################################################################

print(np.ones((3, 5)), end='\n\n')  # creates a 3x5 matrix full of ones
print(np.zeros((3, 5)), end='\n\n')  # creates a 3x5 matrix full of zeros
print(np.identity(3))  # creates the identity matrix
