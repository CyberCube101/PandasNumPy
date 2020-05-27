import numpy as np

x = np.array([3, 5, 1, 6, 2, 7])
print(np.argsort(x))
# [2 4 0 1 3 5]
# This tells us our smallest is in position 2
# Second smallest is in position 4

print(x[x.argsort()])
# [1 2 3 5 6 7]
##############################################

grade = np.array([3, 5, 1, 6, 2, 7])
ages = np.array([8, 10, 6, 11, 7, 12])

sort_index = np.argsort(ages)
print(sort_index)
# we can pass this to sort our grades array
print(grade[sort_index])

#############################################

# to add in the comma's, convert to list

print(list(grade))
