from itertools import combinations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

directory = "//Users/CheickSissoko/Documents/Spring2020_CS6140/homework3/R.csv"

n = 500
mylist = np.array(range(n)) + 1
list_of_pairs = list(combinations(mylist, 2))
file =pd.read_csv(directory, header=None).T
file.columns = mylist

header = ["a,b", "dot Product"]

report = pd.DataFrame([], columns=header)
for each_pair in list_of_pairs:
    key1 = each_pair[0]
    key2 = each_pair[1]
    prod = np.dot(file.get(key1), file.get(key2))
    rep = pd.DataFrame([[each_pair, prod]], columns=header)
    report = report.append(rep)

hist = report.hist(bins=len(list_of_pairs) * 2, cumulative=True, density=True)
plt.show()