import numpy as np


Directory = "/Users/CheickSissoko/Documents/Spring2020_CS6140/homework5/"
S1 = list(open(Directory + "S1.txt").read().strip('\n'))
S2 = list(open(Directory + "S2.txt").read().strip('\n'))

k = 10
t = 5

hash_table = np.zeros(shape=[t,k])
sign_of_t = np.random.uniform(-1,1, size=t)
print(sign_of_t)
print(hash_table)
index = 0
for each_data in S1:
    data_key_index = {}
    j_index = 0
    for each_t in range(t):
        key = each_data + str(each_t)
        if data_key_index.keys().__contains__(key):
            print(hash_table[j_index][data_key_index.get(key)], " before ")
            hash_table[j_index][data_key_index.get(key)] +=1 + + np.sign(sign_of_t[each_t])
            print(hash_table[j_index][data_key_index.get(key)], " after ")
        else:
            # empty_index2 = np.where(hash_table == 0)[0][0]
            empty_index = np.where(hash_table[each_t] == 0)[each_t][0]
            print(empty_index, "empty index")
            data_key_index.update({key: empty_index})
            print(hash_table[j_index, empty_index], "before update")
            print(np.sign(sign_of_t[each_t]), " np sign")
            hash_table[j_index][empty_index] +=1 + np.sign(sign_of_t[each_t])
            print(hash_table[j_index][empty_index], " after update")
        j_index +=1
    print(hash_table)
    index +=1

print(hash_table)


# has_func = np.zeros(shape=[len(S1)])