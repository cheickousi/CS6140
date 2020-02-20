import sys
from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from numpy.linalg import norm
from scipy.spatial.distance import euclidean
from homework4.gonzalez import centers as gonzalez_center

delimiter = "\s+"
directory = "/Users/CheickSissoko/Documents/CS6140/homework4/"
C2 = pd.read_csv(directory + "C2.txt", delimiter=delimiter, header=None)

data = []
index = 1
for rows in C2.itertuples():
    # append the list to the final list
    data.append([rows._2, rows._3])
    index += 1


# For 3-center cost, compute the distance to assigned center for all points,
# and return the maximum value.
# For 3-mean cost, compute the distance to assigned center for all points,
# then square each of these, take their sum, divide by n, then take its square root
def plot(data, centroids):
    plt.scatter(data[:, 0], data[:, 1], marker='.',
                color='gray', label='data points')
    plt.scatter(centroids[:, 0], centroids[:, 1],
                color='red', label='centers')
    plt.title("K means ++")
    plt.legend()
    plt.show()


def get_closest(point, centers):
    '''
    Return the indices the nearest centroids of `p`.
    `centers` contains sets of centroids, where `centers[i]` is
    the i-th set of centroids.
    '''
    best_centers = {}
    index = 0
    for each_center in centers:
        dist = distance(each_center, point)
        best_centers.update({index: dist})
        index += 1
    best = min(best_centers.keys(), key=(lambda k: best_centers[k]))
    return centers[best]


# function to compute euclidean distance
def distance(p1, p2):
    return np.sum((p1 - p2) ** 2)


# initialisation algorithm
def get_center(data, k):
    center = [data[np.random.randint(
        data.shape[0]), :]]
    for _ in range(k - 1):
        dist = []
        for i in range(data.shape[0]):
            point = data[i, :]
            d = sys.maxsize
            for j in range(len(center)):
                temp_dist = distance(point, center[j])
                d = min(d, temp_dist)
            dist.append(d)
        dist = np.array(dist)
        next_centroid = data[np.argmax(dist), :]
        center.append(next_centroid)
    return center


def get_3_center_costs(center, data):
    final_cost = []
    for each_point in data:
        dist = distance(get_closest(each_point, center), each_point)
        final_cost.append(dist)
    cost = np.max(final_cost)
    return cost


def get_3_mean_costs(center, data):
    final_cost = []
    for each_point in data:
        dist = distance(get_closest(each_point, center), each_point)
        final_cost.append(dist)
    mean_cost = np.math.sqrt((1 / len(data)) * np.sum(final_cost))
    return mean_cost


data = np.array(data)
k = 3

gonz_array = np.array(list(gonzalez_center.values()))
epoch = 150

header1 = ['epoch', '3 Mean Cost']
header2 = ['epoch', '3 Center Cost']
report_3_mean_cost = pd.DataFrame([], columns=header1)
report_3_center_cost = pd.DataFrame([], columns=header2)
fraction = 0
for each_epoc in range(epoch):
    center = get_center(data, k)
    mean_cost = get_3_mean_costs(center, data)
    center_cost = get_3_center_costs(center, data)
    rep = pd.DataFrame([[each_epoc, mean_cost]], columns=header1)
    rep2 = pd.DataFrame([[each_epoc, center_cost]], columns=header2)
    report_3_mean_cost = report_3_mean_cost.append(rep)
    report_3_center_cost = report_3_center_cost.append(rep2)
    if (np.sum(center == gonz_array)) == 6:
        fraction += 1

print(fraction, " Out of ", epoch, " Matched")

hist = report_3_mean_cost.hist(bins=epoch *2, cumulative=True, density=True)
plt.title("3 Mean Cost CDF")
# plt.show()

hist2 = report_3_center_cost.hist(bins=epoch *2, cumulative=True, density=True)
plt.title("3 Center Cost CDF")
# plt.show()
