import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def getMisraGries(Data, k_1):
    counter_m = 0
    Labels = np.empty(shape=k_1, dtype=str)
    Counters = np.zeros(shape=k_1)
    for each_character in Data:
        if Labels.__contains__(each_character):
            index = np.argwhere(Labels == each_character)
            Counters[index[0][0]] += 1
        else:
            if Counters.__contains__(0):
                empty_index = np.where(Counters == 0)[0][0]
                Labels[empty_index] = each_character
                Counters[empty_index] = 1
            else:
                Counters -= 1
        counter_m += 1
    return Counters, Labels, (Counters / counter_m) * 100


Directory = "/Users/CheickSissoko/Documents/Spring2020_CS6140/homework5/"
S1 = list(open(Directory + "S1.txt").read().strip('\n'))
S2 = list(open(Directory + "S2.txt").read().strip('\n'))

color_palette_list = ['#009ACD', '#ADD8E6', '#63D1F4', '#0EBFE9',
                      '#C1F0F6', '#0099CC']
k_1 = 9

S1_labels, S1_counters, S1_Counter_ration = getMisraGries(S1, k_1)
S2_labels, S2_counters, S2_Counter_ration = getMisraGries(S2, k_1)

headers =['Labels', 'Counter', 'Counter Radio']
print("S1 Results")
labels = pd.DataFrame(S1_labels)
Counters = pd.DataFrame(S1_counters)
Ratio = pd.DataFrame(S1_Counter_ration)
rep = pd.concat([Counters, labels, Ratio], axis=1, names=headers)
print(rep)


print("S2 Results")
labels = pd.DataFrame(S2_labels)
Counters = pd.DataFrame(S2_counters)
Ratio = pd.DataFrame(S2_Counter_ration)
rep2 = pd.concat([Counters, labels, Ratio], axis=1, names=headers)
print(rep2)

# print(list(Counters))
