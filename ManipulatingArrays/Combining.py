import numpy as np
import numpy.random as npr

array_1 = [[1, 2], [3, 4]]
array_2 = [[5, 6], [7, 8]]

array_3 = np.concatenate((array_1, array_2), axis=0)  # adding rows

print(array_3)
array_4 = np.concatenate((array_1, array_2), axis=1)  # adding columns
print(array_4)

