import numpy as np
from scipy import linalg as LA

A_scv_url = 'http://www.cs.utah.edu/ ̃jeffp/teaching/cs5140/A7/A.csv'


def cleanseUrl(url):
    return url.replace(" ̃", "%7E")


A = np.loadtxt(cleanseUrl(A_scv_url), delimiter=',')

U, s, Vt = LA.svd(A, full_matrices=False)
