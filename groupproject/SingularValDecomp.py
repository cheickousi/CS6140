import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as LA


def computeNorm(A, Ak):
    return LA.norm(A - Ak, 2)


path = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/matrices.csv"

A = np.loadtxt(path, delimiter=',')
# OBTAINING THE SVD OF THE DATA
U, s, Vt = LA.svd(A[:, 1:], full_matrices=False)

from sklearn.decomposition import PCA, TruncatedSVD
import pandas as pd

pca = PCA()
svd = TruncatedSVD(n_components=2)
x_svd = svd.fit_transform(A)
x_svd = pd.DataFrame(x_svd)
# print(x_svd.head())
# print(x_svd.shape)

x_pca = pca.fit_transform(A)
x_pca = pd.DataFrame(x_pca)

x_pca.plot.scatter(0, 1)
# print(x_pca.head())

plt.ylabel("PCA 1")
plt.xlabel("PCA 2")
plt.title("PRINCIPAL COMPONENT ANALYSIS (PCA)")

x_svd.plot.scatter(0, 1)
plt.ylabel("SVD 1")
plt.xlabel("SVD 2")
plt.title("SINGLE VALUE DECOMPOSITION (SVD)")
plt.show()
