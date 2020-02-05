import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev, interp1d

file = "//Users/CheickSissoko/Documents/Spring2020_CS6140/homework3/R.csv"


# f(s) = 1−(1−sb)r
# r = t/b
# b is the number of hashes in a band, and r is the number of rows of bands.


def get_report(s, b, r):
    columns = ["f(s)", "s", "b", "r"]
    fs_report = pd.DataFrame([], columns=columns)
    for each_s in s:
        fs = 1 - np.power((1 - np.power(each_s, b)), r)
        repr = pd.DataFrame([[fs, each_s, b, r]], columns=columns)
        fs_report = fs_report.append(repr)
    return fs_report


t = 160
r = np.arange(5, 100, 15).tolist()


header = ["b", "r"]
report = pd.DataFrame([], columns=header )
s2 = np.arange(0.01, 1, 0.01).tolist()
for each_r in r:
    b = t / each_r
    b_report = get_report(s2, b, each_r)
    x = b_report["s"]
    y = b_report["f(s)"]
    x_new = np.linspace(x.min(), x.max(), 500)
    f = interp1d(x, y, kind='quadratic')
    y_smooth = f(x_new)
    plt.plot(x_new, y_smooth, label = str(each_r))
    plt.legend(loc="best")
    rep = pd.DataFrame([[b, each_r]], columns=header)
    report = report.append(rep)

print(report)
# plt.show()

best_b = 8
best_r = 20
pairs = {"AB": 0.77, "AC": 0.25, "AD": 0.33, "BC": 0.20, "BD": 0.55, "DC": 0.91}

headers = ["Pair", " Similarity", "Probability", "best b" ,"best r"]
b_report = pd.DataFrame([], columns=headers )
for key, each_p in pairs.items():
        fs = 1 - math.pow(1 - math.pow(each_p, best_b), best_r)
        reep = pd.DataFrame([[key, each_p, fs, best_b, best_r]], columns= headers)
        b_report = b_report.append(reep)
    # print(np.round(fs, 3))

print(b_report)