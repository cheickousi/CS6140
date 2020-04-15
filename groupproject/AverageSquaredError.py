import numpy as np
import pandas as pd
from scipy import linalg as LA
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

pd.set_option('display.expand_frame_repr', False)

headers = ['Alpha', 'Test_Average_Squared_Error', 'Training_Average_Squared_Error', 'Test_RMSE']


def getSquaredError(alpha, X_test, Y_test):
    return LA.norm(Y_test.T - predict(alpha, X_test))


def meanSquaredError(alpha, X_test, Y_test):
    return mean_squared_error(Y_test, predict(alpha, X_test))


def RootmeanSquaredError(alpha, X_test, Y_test):
    return np.sqrt(mean_squared_error(Y_test, predict(alpha, X_test)))


def predict(alpha, X):
    bias = np.array(alpha[11])
    alpha_i = np.array(alpha[:11])
    return bias + X @ alpha_i


def generateReport(X_train, Y_train, X_test, Y_test):
    bias = np.ones((X_train.shape[0], 1))
    X_bias = np.hstack((X_train, bias))
    alpha = LA.inv(X_bias.T @ X_bias) @ (X_bias.T @ Y_train)
    report = pd.DataFrame(
        [['alpha_Least_Mean', meanSquaredError(alpha, X_test, Y_test), meanSquaredError(alpha, X_train, Y_train),
          RootmeanSquaredError(alpha, X_test, Y_test)]],
        columns=headers)
    S = {0.000001, 0.0001, 0.001, 0.00001, 0.01, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0}
    for s in S:
        s_alpha = LA.inv(X_bias.T @ X_bias + s * np.identity(12)) @ (X_bias.T @ Y_train)
        error = meanSquaredError(s_alpha, X_test, Y_test)
        err_training = meanSquaredError(s_alpha, X_train, Y_train)
        rootMSE = RootmeanSquaredError(s_alpha, X_test, Y_test)
        rep = pd.DataFrame([['alpha_Ridge_s' + str(s), error, err_training, rootMSE]], columns=headers)
        report = report.append(rep)
    return report


path_X = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/X.csv"
path_y = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/Y.csv"
X = np.loadtxt(path_X, delimiter=',')
Y = np.loadtxt(path_y, delimiter=',')
Cleansed_Y = Y[:, 1:]
Cleansed_X = X[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(Cleansed_X, Cleansed_Y, test_size=0.20, random_state=0)
print(y_test.shape)
print(y_train.shape)
model = generateReport(X_train, y_train, X_test, y_test)
# print(model)

print(model.sort_values(by='Test_Average_Squared_Error', ascending=True))
