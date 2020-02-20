from itertools import combinations
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from numpy.linalg import norm
from scipy.spatial.distance import euclidean

delimiter = "\s+"
directory = "/Users/CheickSissoko/Documents/CS6140/homework4/"
C1 = pd.read_csv(directory + "C1.txt", delimiter=delimiter, header=None)

data_points = {}
index = 1
for rows in C1.itertuples():
    # append the list to the final list
    data_points.update({index: (rows._2, rows._3)})
    index += 1


def distance(p1, p2):
    return np.sum((np.array(p1) - np.array(p2)) ** 2)


def remove_pairs(cluster, remain):
    pairs = list(combinations(cluster, 2))
    for each_pair in pairs:
        try:
            remain.remove(each_pair)
        except:
            pass
    return remain


def get_hierarchical_key(new_cluster, clusters):
    key_re = []
    for key, value in clusters.items():
        for each_point in value:
            if each_point in new_cluster:
                key_re.append(key)
    return key_re


def get_single_link_shortest_points(pairs):
    distances_between_all_pairs = {}
    for each_pair in pairs:
        vector_a = data_points.get(each_pair[0])
        vector_b = data_points.get(each_pair[1])
        distances_between_all_pairs.update({each_pair: distance(vector_a, vector_b)})
    key_min = min(distances_between_all_pairs.keys(), key=(lambda k: distances_between_all_pairs[k]))
    print("the key is ", key_min)
    return key_min


def get_complete_link_shortest_points(pairs):
    distances_between_all_pairs = {}
    for each_pair in pairs:
        vector_a = data_points.get(each_pair[0])
        vector_b = data_points.get(each_pair[1])
        distances_between_all_pairs.update({each_pair: distance(vector_a, vector_b)})
    key_max = max(distances_between_all_pairs.keys(), key=(lambda k: distances_between_all_pairs[k]))
    return key_max


def merge_cluster(cluster_a, cluster_b):
    return tuple(set(cluster_a).union(cluster_b))


def get_mean_link_shortest_points(pairs):
    distances_between_all_pairs = {}
    for each_pair in pairs:
        vector_a = data_points.get(each_pair[0])
        vector_b = data_points.get(each_pair[1])
        a1 = (1 / len(vector_a)) * np.sum(vector_a)
        a2 = (1 / len(vector_b)) * np.sum(vector_b)
        distances_between_all_pairs.update({each_pair: norm(a1 - a2, None)})
        key_min = min(distances_between_all_pairs.keys(), key=(lambda k: distances_between_all_pairs[k]))
    return key_min


def gerante_report(clusters):
    final_header = ['Cluster_Group', "Point", "X_values", "Y_values"]
    report = pd.DataFrame([], columns=final_header)
    index = 1
    for key, points in clusters.items():
        for each_point in points:
            for rows in C1.itertuples():
                if rows._1 == each_point:
                    rep = pd.DataFrame([["Cluster_" + str(index), rows._1, rows._2, rows._3]], columns=final_header)
                    report = report.append(rep)
        index += 1
    return report


# Single Link Implementation

remaining_clusters = set(range(1, len(data_points.keys()) + 1))
remaining_pairs_of_clusters = list(combinations(remaining_clusters, 2))
header = ["hierarchy", "Clusters_Points"]
clusters = {i: (j,) for i, j in enumerate(data_points.keys())}
while len(clusters) > 4:
    next_closest_clusters = get_single_link_shortest_points(remaining_pairs_of_clusters)
    key = get_hierarchical_key(next_closest_clusters, clusters)
    key = list(set(key))
    if len(key) == 1:
        clusters.update({key[0]: merge_cluster(clusters[key[0]], next_closest_clusters)})
        remaining_pairs_of_clusters = remove_pairs(clusters[key[0]], remaining_pairs_of_clusters)
        remaining_pairs_of_clusters = remove_pairs(next_closest_clusters, remaining_pairs_of_clusters)
    else:
        index = 0
        for each_key in key:
            if not index == 0:
                clusters.update({key[0]: merge_cluster(clusters[key[0]], clusters.get(each_key))})
                remaining_pairs_of_clusters = remove_pairs(clusters[key[0]], remaining_pairs_of_clusters)
                remaining_pairs_of_clusters = remove_pairs(next_closest_clusters, remaining_pairs_of_clusters)
                clusters.pop(each_key)
            index += 1
report = gerante_report(clusters)
print("######### Simple Link Report ###########")
print(report)
sns.scatterplot(data=report, x='X_values', y='Y_values', hue='Cluster_Group')
plt.title("Simple Link Cluster")
plt.show()
# Complete Link Implementation

remaining_clusters = set(range(1, len(data_points.keys()) + 1))
remaining_pairs_of_clusters = list(combinations(remaining_clusters, 2))
header = ["hierarchy", "Clusters_Points"]
clusters = {i: (j,) for i, j in enumerate(data_points.keys())}
while len(clusters) > 4:
    next_closest_clusters = get_complete_link_shortest_points(remaining_pairs_of_clusters)
    key = get_hierarchical_key(next_closest_clusters, clusters)
    key = list(set(key))
    if len(key) == 1:
        clusters.update({key[0]: merge_cluster(clusters[key[0]], next_closest_clusters)})
        remaining_pairs_of_clusters = remove_pairs(clusters[key[0]], remaining_pairs_of_clusters)
        remaining_pairs_of_clusters = remove_pairs(next_closest_clusters, remaining_pairs_of_clusters)
    else:
        index = 0
        for each_key in key:
            if not index == 0:
                clusters.update({key[0]: merge_cluster(clusters[key[0]], clusters.get(each_key))})
                remaining_pairs_of_clusters = remove_pairs(clusters[key[0]], remaining_pairs_of_clusters)
                remaining_pairs_of_clusters = remove_pairs(next_closest_clusters, remaining_pairs_of_clusters)
                clusters.pop(each_key)
            index += 1
print(clusters)

print("######### Complete Link Report ###########")
print(report)
sns.scatterplot(data=report, x='X_values', y='Y_values', hue='Cluster_Group')
plt.title("Complete Link Cluster")
plt.show()
# Mean Link

remaining_clusters = set(range(1, len(data_points.keys()) + 1))
remaining_pairs_of_clusters = list(combinations(remaining_clusters, 2))
header = ["hierarchy", "Clusters_Points"]
clusters = {i: (j,) for i, j in enumerate(data_points.keys())}
while len(clusters) > 4:
    next_closest_clusters = get_mean_link_shortest_points(remaining_pairs_of_clusters)
    key = get_hierarchical_key(next_closest_clusters, clusters)
    key = list(set(key))
    if len(key) == 1:
        clusters.update({key[0]: merge_cluster(clusters[key[0]], next_closest_clusters)})
        remaining_pairs_of_clusters = remove_pairs(clusters[key[0]], remaining_pairs_of_clusters)
        remaining_pairs_of_clusters = remove_pairs(next_closest_clusters, remaining_pairs_of_clusters)
    else:
        index = 0
        for each_key in key:
            if not index == 0:
                clusters.update({key[0]: merge_cluster(clusters[key[0]], clusters.get(each_key))})
                remaining_pairs_of_clusters = remove_pairs(clusters[key[0]], remaining_pairs_of_clusters)
                remaining_pairs_of_clusters = remove_pairs(next_closest_clusters, remaining_pairs_of_clusters)
                clusters.pop(each_key)
            index += 1
report = gerante_report(clusters)
print("######### Mean Link Report ###########")
print(report)
sns.scatterplot(data=report, x='X_values', y='Y_values', hue='Cluster_Group')
plt.title("Mean Link Cluster")
# plt.show()
