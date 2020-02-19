import pandas as pd
import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

# %matplotlib inline
from scipy.spatial.distance import euclidean


def returnSumWeight(dict):
    sum = 0
    for i in dict.values():
        sum += i
    return sum


delimiter = "\s+"
directory = "/Users/CheickSissoko/Documents/CS6140/homework4/"
C2 = pd.read_csv(directory + "C2.txt", delimiter=delimiter, header=None)

data_points = {}
data2 = []
index = 1
for rows in C2.itertuples():
    # append the list to the final list
    data_points.update({index: (rows._2, rows._3)})
    data2.append([rows._2, rows._3])
    index += 1

data = np.array(data2)


# importing dependencies


# function to plot the selected centroids
def plot(data, centroids):
    plt.scatter(data[:, 0], data[:, 1], marker='.',
                color='gray', label='data points')
    plt.scatter(centroids[:, 0], centroids[:, 1],
                color='red', label='centers')
    plt.title("K means ++")
    plt.legend()
    plt.show()


# function to compute euclidean distance
def distance(p1, p2):
    return np.sum((p1 - p2) ** 2)


# initialisation algorithm
def initialize(data, k):
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
    for each_center in center:
        cost = []
        for each_point in data:
            cost.append(distance(each_center, each_point))
        final_cost.append(np.max(cost))
    return final_cost


def get_3_mean_costs(center, data):
    final_cost = []
    for each_center in center:
        cost = []
        for each_point in data:
            dist = distance(each_center, each_point) ** 2
            cost.append(dist)
        mean_cost = np.math.sqrt((1 / len(data)) * np.sum(cost))
        final_cost.append(mean_cost)
    return final_cost


# call the initialize function to get the centroids
centroids = initialize(data, k=3)

plot(data, np.array(centroids))

def get_closest(p, centers):
    '''
    Return the indices the nearest centroids of `p`.
    `centers` contains sets of centroids, where `centers[i]` is
    the i-th set of centroids.
    '''
    best = [0] * len(centers)
    closest = [np.inf] * len(centers)
    for idx in range(len(centers)):
        for j in range(len(centers[0])):
            temp_dist = distance(p - centers[idx][j])
            if temp_dist < closest[idx]:
                closest[idx] = temp_dist
                best[idx] = j
    return best


