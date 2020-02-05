from itertools import combinations
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_angular_report(list_of_pairs, data):
    header = ["Pairs", "Angular Similarity"]
    report = pd.DataFrame([], columns=header)
    number_above = 0
    for each_pair in list_of_pairs:
        key1 = each_pair[0]
        key2 = each_pair[1]
        dot_prod = np.dot(data.get(key1), data.get(key2))
        similarity = 1 - (1 / np.pi) * np.arccos(dot_prod)
        rep = pd.DataFrame([[each_pair, similarity]], columns=header)
        report = report.append(rep)
        if float(similarity) >= float(0.85):
            number_above += 1
    hist = report.hist(bins=len(list_of_pairs) * 2, cumulative=True, density=True)
    return hist, number_above


directory = "//Users/CheickSissoko/Documents/Spring2020_CS6140/homework3/R.csv"

n = 500
mylist = np.array(range(n)) + 1
list_of_pairs = list(combinations(mylist, 2))
file = pd.read_csv(directory, header=None).T
file.columns = mylist


# historigram, number_above = generate_angular_report(list_of_pairs, file)
# print(number_above)

from homework3.random_direction import list_of_pairs as list_pairs_B, myList_vectors

historigram2, number_above2 = generate_angular_report(list_pairs_B, myList_vectors)

print(number_above2)

plt.show()
