import numpy as np
import pandas as pd
from numpy import linalg as LA

X = u'http://www.cs.utah.edu/~jeffp/teaching/cs5140/A6/X.csv'
Y = u'http://www.cs.utah.edu/ ̃jeffp/teaching/cs5140/A6/y.csv'


def cleanseUrl(url):
    return url.replace(" ̃", "%7E")


headers = ['Alpha', 'error']
X = np.loadtxt(cleanseUrl(X), delimiter=',')
Y = np.loadtxt(cleanseUrl(Y), delimiter=',')
ones = np.ones((X.shape[0], 1))
X_with_bias = np.hstack((X, ones))

Xt = np.transpose(X_with_bias)
XtX = np.dot(Xt, X_with_bias)
Yt = np.transpose(Y)
alpha = LA.inv(X_with_bias.T @ X_with_bias) @ (X_with_bias.T @ Y.T)

alpha_zero = np.array(alpha[50])
alpha_i = np.array(alpha[:50])
Y_prediction = alpha_zero + X @ alpha_i
error1 = LA.norm(Y - Y_prediction)

report = pd.DataFrame([['alpha_least_mean', error1]], columns=headers)

S = {0.2, 0.4, 0.8, 1.0, 1.2, 1.4, 1.6}
for s in S:
    s_alpha = LA.inv(X_with_bias.T @ X_with_bias + s * np.identity(51)) @ (X_with_bias.T @ Y.T)
    alpha_zero = np.array(s_alpha[50])
    alpha_i = np.array(s_alpha[:50])
    Y_prediction = alpha_zero + X @ alpha_i
    error = LA.norm(Y - Y_prediction)
    rep = pd.DataFrame([['alpha' + str(s), error]], columns=headers)
    report = report.append(rep)

print(report)
