import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

a = np.full(4, True, dtype=bool)

b = np.ones(4, dtype=bool)

c = np.zeros(4, dtype=int)

# Random booleans array

y = npr.randint(0, 2, size=10, dtype=int)

data = npr.normal(100, 15, size=25)  # mean 100, SD 15
mask = data > 100
print(data[mask])

#####################################################

log_and = np.logical_and(data > 100, data < 110)
print(data[log_and])

log_or = np.logical_or(data > 115, data < 85)
print(data[log_or])

#####################################################

# we can test if the values in between 2 arrays
# with an absolute tolerance of say 1

rand = npr.randint(1, 11, 25)
close = data + rand
print(np.allclose(data, close, atol=5))
print(np.isclose(data, close, atol=5))
print(np.count_nonzero(np.isclose(data, close, atol=5)))  # add up all the trues
