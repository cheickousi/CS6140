import mmh3
import numpy as np

Directory = "/Users/CheickSissoko/Documents/Spring2020_CS6140/homework5/"
S1 = list(open(Directory + "S1.txt").read().strip('\n'))
S2 = list(open(Directory + "S2.txt").read().strip('\n'))

k = 10
t = 5


def estimate_count(key, hash_table):
    previous_low = 0
    for i in range(0, t):
        index = mmh3.hash(key, seed=i) % k
        table_value = hash_table[i][index]
        if i == 0:
            previous_low = table_value
        if table_value < previous_low:
            previous_low = table_value
    return previous_low


def generateMinHashTable(Data):
    hash_table = np.zeros(shape=[t, k])
    index = 0
    for each_data in Data:
        for each_t in range(t):
            key = mmh3.hash(each_data, seed=each_t) % k
            hash_table[each_t][key] += 1
        index += 1
    return hash_table, index


print("Generating S1 Data")
s1hash, index1 = generateMinHashTable(S1)

count_a = estimate_count("a", s1hash)
count_b = estimate_count("b", s1hash)
count_c = estimate_count("c", s1hash)

print("The count of a", count_a)
print("The Rate of a", (count_a / index1) * 100)
print("The count of b", count_b)
print("The Rate of b", (count_b / index1) * 100)
print("The count of c", count_c)
print("The Rate of c", (count_c / index1) * 100)

print("Generating S2 Data")
s2hash, index2 = generateMinHashTable(S2)

count_a = estimate_count("a", s2hash)
count_b = estimate_count("b", s2hash)
count_c = estimate_count("c", s2hash)
print("The count of a", count_a)
print("The Rate of a", (count_a / index1) * 100)
print("The count of b", count_b)
print("The Rate of b", (count_b / index1) * 100)
print("The count of c", count_c)
print("The Rate of c", (count_c / index1) * 100)
