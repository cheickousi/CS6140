from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from numpy.linalg import norm
from scipy.spatial.distance import euclidean
from homework4.gonzalez import centers as gonzalez_center
from homework4.kmeansplus import get_3_center_costs, get_center

delimiter = "\s+"
directory = "/Users/CheickSissoko/Documents/CS6140/homework4/"
C2 = pd.read_csv(directory + "C2.txt", delimiter=delimiter, header=None)


# print(C2)
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


def distance(p1, p2):
    return np.sum((p1 - p2) ** 2)


def plot(data, centroids):
    plt.scatter(data[:, 0], data[:, 1], marker='.',
                color='gray', label='data points')
    plt.scatter(centroids[:, 0], centroids[:, 1],
                color='red', label='centers')
    plt.title("K means ++")
    plt.legend()
    plt.show()


def get_3_mean_costs(center, data):
    final_cost = []
    for each_point in data:
        dist = distance(get_closest(each_point, center), each_point)
        final_cost.append(dist)
    mean_cost = np.math.sqrt((1 / len(data)) * np.sum(final_cost))
    return mean_cost


def get_lloyds_centers(data, initial_center):
    for _ in range(epoch):
        center_points_mapping = {}
        for each_point in data.values():
            closest_center = get_closest(each_point, initial_center)
            center_points_mapping.update({each_point: closest_center})

        index = 0
        for each_center in initial_center:
            list_of_assigned_points = []
            for point, center in center_points_mapping.items():
                if all(each_center == center):
                    list_of_assigned_points.append(np.array(point))
            initial_center[index] = np.average(list_of_assigned_points, axis=0)
            index += 1
    return initial_center


data_points = {}
data = []
index = 1
for rows in C2.itertuples():
    # append the list to the final list
    data_points.update({index: (rows._2, rows._3)})
    data.append([rows._2, rows._3])
    index += 1
epoch = 20
data = np.array(data)

k = 3
center = {1: data_points.get(1), 2: data_points.get(2), 3: data_points.get(3)}
centers = np.array(list(center.values()))

lloyd_center = get_lloyds_centers(data_points, centers)

print("Run Lloyds Algorithm with C initially with points indexed {1,2,3}. Report the final subset and the 3-means cost",
      "\n")
print("centers are")
print(lloyd_center, "\n")

print("3-means cost")
print(get_3_mean_costs(lloyd_center, data))

gonz_center = np.array(list(gonzalez_center.values()))

print("Run Lloyds Algorithm with C initially as the output of Gonzalez above. Report the final subset and the 3-means "
      "cost.")
print("centers are")
lloyd_gonz = get_lloyds_centers(data_points, gonz_center)
print(lloyd_gonz, "\n")
print("3-means cost")
print(get_3_mean_costs(lloyd_gonz, data))


print("Run Lloyds Algorithm with C initially as the output of each run of k-Means++ above. Plot a cumu- lative "
      "density function of the 3-means cost.")
header1 = ['epoch', '3 Mean Cost']
report_3_mean_cost = pd.DataFrame([], columns=header1)
fraction = 0

epoch2 = 150
for each_epoc in range(epoch2):
    k_means_center = get_center(data, k)
    lloyd = get_lloyds_centers(data_points, k_means_center)
    mean_cost = get_3_mean_costs(lloyd, data)
    rep = pd.DataFrame([[each_epoc, mean_cost]], columns=header1)
    report_3_mean_cost = report_3_mean_cost.append(rep)
    if (np.sum(k_means_center == lloyd)) == 6:
        fraction += 1

print(fraction, " Out of ", epoch2, " Matched")

hist = report_3_mean_cost.hist(bins=epoch2 * 2, cumulative=True, density=True)
plt.title("3 Mean Cost CDF for LLoyd")
plt.show()


