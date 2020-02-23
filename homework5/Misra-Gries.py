import numpy as np
import matplotlib.pyplot as plt

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

plt.bar( S1_Counter_ration, S1_labels,color = color_palette_list)
plt.title('S1 Misra Gries')
plt.show()
plt.bar(S2_Counter_ration, S2_labels,color = color_palette_list)
plt.title('S2 Misra Gries')
# print(np.sum(S1_Counter_ration))
plt.show()

# print(list(Counters))
