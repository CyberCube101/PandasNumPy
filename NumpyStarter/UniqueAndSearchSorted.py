import numpy as np
import numpy.random as npr
from itertools import combinations

available = [x[0] + x[1] + x[2] for x in combinations("ABCDEFGHIJ", 3)]

symbols = npr.choice(available, 60)
# print(len(symbols))
# symbols = np.unique(symbols)
# print(len(symbols))

# lets see where in the index these values are
# this gives 2 arrays, 1 original and 2nd are indexes
z, k = np.unique(symbols, return_index=True)

#####################################################
# Return count of obs

a, b = np.unique(symbols, return_counts=True)
print(a)
print(b)
