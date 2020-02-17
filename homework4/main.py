import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
import scipy.cluster.hierarchy as shc

delimiter = "\s+"
directory = "/Users/CheickSissoko/Documents/CS6140/homework4/"
C1 = pd.read_csv(directory + "C1.txt", delimiter=delimiter, header=None)


print(C1)
# plt.figure(figsize=(10, 4))
# # plt.title("Dendrograms")
# dend = shc.dendrogram(shc.linkage(C1, method='ward'))
# plt.show()


