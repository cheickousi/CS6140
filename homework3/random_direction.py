from itertools import combinations
import pandas as pd
import numpy as np
from numpy import linalg as LA
from random import seed
from random import gauss
import matplotlib.pyplot as plt

np.random.seed(2)
# seed random number generator
seed(2)


# generates a uniform random variable between 0 and 1.

def generate_single_random_uniform_vector(dimension):
    output = []
    for _ in range(dimension):
        output.append(gauss(0, 1))
    return output


d = 100
t = 160

myList_vectors = {}
for each_t in range(t):
    myList_vectors.update({each_t + 1: generate_single_random_uniform_vector(d)})

mylist = np.array(range(d)) + 1
list_of_pairs = list(combinations(mylist, 2))

header = ["Pair of t", "dot Product"]

report = pd.DataFrame([], columns=header)
for each_pair in list_of_pairs:
    key1 = each_pair[0]
    key2 = each_pair[1]
    prod = np.dot(myList_vectors.get(key1), myList_vectors.get(key2))
    rep = pd.DataFrame([[each_pair, prod]], columns=header)
    report = report.append(rep)

hist = report.hist(bins=len(list_of_pairs) * 2, cumulative=True, density=True)

plt.show()

# generate random Gaussian values
# generate some Gaussian values
