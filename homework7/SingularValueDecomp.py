import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import linalg as LA

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

A_scv_url = 'http://www.cs.utah.edu/ ̃jeffp/teaching/cs5140/A7/A.csv'


def cleanseUrl(url):
    return url.replace(" ̃", "%7E")


def reduceDimension(k, U, S, Vt):
    Uk = U[:k, :k]
    Sk = S[:k]
    Vtk = Vt[:k, :]
    Ak = Uk @ Sk @ Vtk
    return Ak


def computeNorm(A, Ak):
    return LA.norm(A - Ak, 2)


A = np.loadtxt(cleanseUrl(A_scv_url), delimiter=',')

U, s, Vt = LA.svd(A, full_matrices=False)

k = 20
header = ['k', 'L2A-Ak', '10L2A', 'diff']
report = pd.DataFrame([], columns=header)

for eack_k in range(1, k + 1):
    Ak = reduceDimension(eack_k, U, s, Vt)
    norm = computeNorm(A, Ak)
    compar = LA.norm(A, 2) * 1.1
    rep = pd.DataFrame([[eack_k, norm, compar, norm - compar]], columns=header)
    report = report.append(rep)

print(report)

print("\nB (10 points): Find the smallest value k so that the L2 norm of A-Ak is less than 10% that of A; k might or "
      "might not be larger than 10\n")
print(report[report['diff'] <= 0])

print("\nPlot the points in 2 dimensions in the way that minimizes the sum of residuals squared, and describe briefly "
      "how you did it\n")

Vtk = Vt[:2, :]

X = Vtk[0, :]
Y = Vtk[1, :]

plt.scatter(x=X, y=Y)
# plt.show()
