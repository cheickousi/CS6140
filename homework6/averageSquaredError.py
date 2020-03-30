import numpy as np
import pandas as pd
from numpy import linalg as LA
from sklearn.metrics import mean_squared_error

X = u'http://www.cs.utah.edu/~jeffp/teaching/cs5140/A6/X.csv'
Y = u'http://www.cs.utah.edu/ ̃jeffp/teaching/cs5140/A6/y.csv'
headers = ['Alpha', 'error']


def cleanseUrl(url):
    return url.replace(" ̃", "%7E")


def meanSquaredError(alpha, X_test, Y_test):
    return mean_squared_error(Y_test, predict(alpha, X_test))


def predict(alpha, X):
    bias = np.array(alpha[50])
    alpha_i = np.array(alpha[:50])
    return bias + X @ alpha_i


def generateReport(X_train, Y_train, X_test, Y_test):
    bias = np.ones((X_train.shape[0], 1))
    X_bias = np.hstack((X_train, bias))
    alpha = LA.inv(X_bias.T @ X_bias) @ (X_bias.T @ Y_train.T)
    report = pd.DataFrame([['alpha_Least_Mean', meanSquaredError(alpha, X_test, Y_test)]], columns=headers)
    S = {0.2, 0.4, 0.8, 1.0, 1.2, 1.4, 1.6}
    for s in S:
        s_alpha = LA.inv(X_bias.T @ X_bias + s * np.identity(51)) @ (X_bias.T @ Y_train.T)
        error = meanSquaredError(s_alpha, X_test, Y_test)
        rep = pd.DataFrame([['alpha_Ridge_s' + str(s), error]], columns=headers)
        report = report.append(rep)
    return report


X = np.loadtxt(cleanseUrl(X), delimiter=',')
Y = np.loadtxt(cleanseUrl(Y), delimiter=',')
X = np.array(X)
Y = np.array(Y)
ones = np.ones((X.shape[0], 1))
X_with_bias = np.hstack((X, ones))
X1 = X[:66, :]
X1_test = X[66:, :]
Y1 = Y[:66]
Y1_test = Y[66:]

X2 = X[33:, :]
X2_test = X[:66, :]
Y2 = Y[33:]
Y2_test = Y[:66]
X3 = np.vstack((X[:33, :], X[66:, :]))
X3_test = np.vstack((X[33:, :], X[:66, :]))
Y3 = np.concatenate((Y[:33], Y[66:]))
Y3_test = np.concatenate((Y[33:], Y[:66]))

Best_model = pd.DataFrame([], columns=headers)

print("################## X1 report #################")

X1_report = generateReport(X1, Y1, X1_test, Y1_test)
Best_model = Best_model.append(X1_report)
print(X1_report)

print("################ X2 report  ##############")
X2_report = generateReport(X2, Y2, X2_test, Y2_test)
Best_model = Best_model.append(X2_report)
print(X2_report)
print("################# X3 report####################")
X3_report = generateReport(X3, Y3, X3_test, Y3_test)
Best_model = Best_model.append(X3_report)
print(X3_report)
print("################# Best Model ####################")
print(Best_model.sort_values(by='error', ascending=False).groupby('Alpha').mean())
