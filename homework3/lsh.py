import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev

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
r = 85
b = t / r
r2 = np.power(1 / r, 1 / b)
b2 = - math.log(t, r2)
s = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

b_report = get_report(s, b, r)
b2_report = get_report(s, b2, r2)
print(b_report)

x = b_report["s"]
y = b_report["f(s)"]
print(b2_report)
plt.figure()
plt.plot(x, y)
b2_report.plot(kind = "line", x="s",y="f(s)",color="red" )
plt.show()
