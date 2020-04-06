import numpy as np
import pandas as pd
from scipy import linalg as LA

from homework7.SingularValueDecomp import reduceDimension

A_scv_url = 'http://www.cs.utah.edu/ ̃jeffp/teaching/cs5140/A7/A.csv'


def cleanseUrl(url):
    return url.replace(" ̃", "%7E")


def freq_dir(A, l):
    r = A.shape[0]
    c = A.shape[1]
    B = np.zeros([l * 2, c])
    B[: l - 1, :] = A[: l - 1, :]
    zerorows = l + 1
    for i in range(l - 1, r):
        """
      implement the algorithm 16.2.1 in L16 MatrixSketching in Data Mining course webpage
          insert ith row into a zero-value row of the mat_b
          if B has no zero-valued rows ( can be ketp track with counter) then:
            U,S,V = svd(mat_b)  using  U,S,V = np.linalg.svd(mat_b,full_matrices = False)
            ...
            procedure same as the algorithm 16.2.1
            ...
      """
        if zerorows > 0:
            B[B.shape[0] - zerorows, :] = A[i, :]
            zerorows -= 1
        else:
            U, S, V = np.linalg.svd(B, full_matrices=False)
            singular_value = np.power(S[l], 2)
            new_matrix = np.power(S, 2) - singular_value
            new_matrix_squared = np.sqrt(new_matrix)
            S_prime = np.nan_to_num(np.diag(new_matrix_squared))
            B = S_prime @ V
            zerorows = l
    return B


A = np.loadtxt(cleanseUrl(A_scv_url), delimiter=',')

l = 19
at_most_error = np.power(LA.norm(A, 'fro'), 2) / 10

header = ['L', 'Error']
report = pd.DataFrame([], columns=header)
for each_l in range(1, l + 1):
    B = freq_dir(A, each_l)
    error = LA.norm(A.T @ A - B.T @ B)
    rep = pd.DataFrame([[each_l, error]], columns=header)
    report = report.append(rep)
print(report)

print("\nHow large does l need to be for the above error to be at most ∥A∥2F /10?\n")
print(at_most_error)
print(report[report['Error'] <= at_most_error])

print("\nHow large does l need to be for the above error to be at most ∥A−Ak∥2F/10(fork=2)?\n")
U, s, Vt = LA.svd(A, full_matrices=False)
Ak = reduceDimension(2, U, s, Vt)
at_most_error2 = np.power(LA.norm(A - Ak, 'fro'), 2) / 10
print(at_most_error2)
print(report[report['Error'] <= at_most_error2])
