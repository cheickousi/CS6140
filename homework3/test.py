import numpy as np
from numpy import linalg as LA

# generates a uniform random variable between 0 and 1.
d = 10

randuni = np.random.uniform(low=0, high=1, size=d)

for each_x in randuni:
    nor = np.exp(- np.power(LA.norm(each_x), 2) / 2)
    deno = np.power(2 * np.pi, d / 2)
    gausian_x = (1/deno) * nor
    print(gausian_x)
