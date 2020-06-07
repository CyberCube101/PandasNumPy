import numpy as np
import numpy.random as npr

x = npr.randint(-10, 10, size=100)
# print(x)

# get obs that meet an upper and lower bound

x = np.clip(x, -4, 0)
# print(x)

#######################################################
# Random Sampling

y = npr.randint(1000, size=100)
# print(y)

z = npr.choice(y, 20, replace=False)
# print(z)

########################################################
# Discrete probability distribution, non-uniform

a = npr.choice(np.arange(1, 7), 1, p=[0.2, 0.1, 0.3, 0.15, 0.05, 0.2])
# this is saying the prob of getting a 1 is 0.2
# the prob of getting at 2 is 0.1 etc. We are choosing 1 number from that

# print(a)

#######################################################
# Stable Sample

new = npr.random(100)
sample = np.argsort(new)
print(new[sample])  # sorted random array
