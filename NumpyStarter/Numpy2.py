# subsetting arrays

import numpy as np

data = np.random.randint(1, 10, size=15)
print(data)
print(data[0])
print(data[:3])

# create a 3 by 5

data = data.reshape(3, 5)
print(data)

# if we slice on a matrix, we ge the whole row
print(data[0])

# to get first column, we use the colon with a comma
print(data[:, 0])

# for a single element, pass in the co-ordinates
print(data[0, 0])  # rc
