import numpy as np
from matplotlib import pyplot as plt
from scipy import linalg as LA


def reduceDimension(k, U, S, Vt):
    Uk = U[:k, :k]
    # Sk = S[:k]
    Vtk = Vt[:k, :]
    Ak = Uk @ Vtk
    return Ak


def computeNorm(A, Ak):
    return LA.norm(A - Ak, 2)


path = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/matrices.csv"

A = np.loadtxt(path, delimiter=',')
# OBTAINING THE SVD OF THE DATA
U, s, Vt = LA.svd(A[:, 1:], full_matrices=False)

print(U.shape)
print(s.shape)
print(Vt.shape)
Vtk = Vt[:2, :]
Ak = reduceDimension(2, U, s, Vt)

print(Ak.shape)

X = Vtk[0, :]
Y = Vtk[1, :]

print(X)
print(Y)

plt.scatter(x=X, y=Y)
plt.show()
