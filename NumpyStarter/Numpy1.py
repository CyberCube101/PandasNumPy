import numpy as np

# numpy is computationally faster than lists
# Data must be same type
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
print(max_32)
# 64 bit range
bit_64 = 2 ** 64 - 1
max_64 = bit_64 / 2
print(max_64)
#################################################################
