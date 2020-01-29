import numpy as np
from string import punctuation
import pandas as pd
import time

np.random.seed(1)
from homework2.inputs import D1, D2


def split_char(k_grams, string):
    string = remove_all_punctuation(string)
    my_out = np.unique([(string[i:i + k_grams]) for i in range(len(string) + 1 - k_grams)])  #
    return my_out


def remove_all_punctuation(string):
    return "".join((char for char in string if char not in punctuation))


def get_report(number_of_f):
    k_grams = 3
    headers = ["t", "JS(D1, D2)", " Time Elapsed"]
    report = pd.DataFrame([], columns=headers)
    a_hash = split_char(k_grams, D1)
    b_hash = split_char(k_grams, D2)
    for each_hash_q in number_of_f:
        startTime = time.time()
        my_domain = get_domain(a_hash, b_hash, each_hash_q)
        a_sign = get_min_hash_signature(my_domain, a_hash)
        b_sign = get_min_hash_signature(my_domain, b_hash)
        total_k = my_domain.shape[1]
        intersection = np.intersect1d(a_sign, b_sign).__len__()
        jacc = intersection / total_k
        endTime = time.time()
        timeElapsed1 = endTime - startTime
        rep = pd.DataFrame([[each_hash_q, jacc, timeElapsed1]], columns=headers)
        report = report.append(rep)
    return report


def get_min_hash_signature(matrix, my_hash):
    pd_vector = pd.DataFrame([matrix[my_hash].iloc[0]], columns=my_hash)
    updated_domain = matrix[my_hash]
    for index, row in updated_domain.iterrows():
        pd_vector = row.where(row[my_hash] < pd_vector.iloc[0], row[my_hash])
    return pd_vector


def get_domain(a_hash, b_hash, hash_funct):
    domain = np.unique(np.hstack([a_hash, b_hash]))
    hash_function_mapping = np.random.randint(low=1, high=np.power(domain.shape[0], 2),
                                              size=[hash_funct, domain.shape[0]])
    domain_matrix = pd.DataFrame([], columns=domain)
    for each_row in hash_function_mapping:
        new_row = pd.DataFrame([each_row], columns=domain)
        domain_matrix = domain_matrix.append([new_row])
    return domain_matrix


# generating permuation functions


number_hash_functions = [10, 20, 40, 60, 150, 300, 600, 900, 1000 ]

number_hash_functions2 = [20, 60, 150, 300, 600]


print(get_report(number_hash_functions2))

print(get_report(number_hash_functions), '\n')
