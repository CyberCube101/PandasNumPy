import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt

x = npr.standard_normal(5000)
print({"{:15.10f}".format(x.mean())})
print({"{:15.10f}".format(x.std())})

# {'  -0.0006020942'}  its not quite zero
# {'   0.9997493059'}  its not quite 1

plt.hist(x, bins=50)
# plt.show()

# We need to normalise to make 0 and 1

y = np.concatenate([x, -x])
print({"{:15.10f}".format(y.mean())})

plt.hist(y, bins=50)
# plt.show()

# now to normalise
z = (y - y.mean()) / y.std()
print({"{:15.10f}".format(z.mean())})
print({"{:15.10f}".format(z.std())})
plt.hist(z, bins=50)
plt.show()

##############################################

# To isolate the randomness for sensitivity analysis, use seed
c = npr.random(10)
print(c)

# lets say we want to keep a stable sample, so that we can see
# the impact of other variables

npr.seed(42)  # 42 is common as that the meaning on life :-)

d = npr.random(10)
print(d)
