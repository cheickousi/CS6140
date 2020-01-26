import numpy as np
from string import punctuation
import pandas as pd
# np.random.seed(2)
from homework2.inputs import D1, D2


def split_char(k_grams, string):
    string = remove_all_punctuation(string)
    my_out = np.unique([(string[i:i + k_grams]) for i in range(len(string) + 1 - k_grams)])
    return my_out


def remove_all_punctuation(string):
    return "".join((char for char in string if char not in punctuation))


def get_min_hash_signature(matrix, my_hash):
    pd_vector = pd.DataFrame([matrix[my_hash].iloc[0]], columns=my_hash)
    updated_domain = matrix[my_hash]
    for index, row in updated_domain.iterrows():
        pd_vector = row.where(pd_vector.iloc[0] > row[my_hash], pd_vector.iloc[0])
    return pd_vector.values


def get_domain(text, text2, k_grams, hash_funct):
    a_hash = split_char(k_grams, text)
    b_hash = split_char(k_grams, text2)
    domain = np.unique(np.hstack([a_hash, b_hash]))
    hash_function_mapping = np.random.randint(low=1, high=np.power(domain.shape[0], 2), size=[hash_funct, domain.shape[0]])
    domain_matrix = pd.DataFrame([], columns=domain)
    for each_row in hash_function_mapping:
        new_row = pd.DataFrame([each_row], columns=domain)
        domain_matrix = domain_matrix.append([new_row])
    return domain_matrix


# generating permuation functions


number_hash_functions = [20, 60, 150, 300, 600]
k_grams = 3
for each_hash_q in number_hash_functions:
    my_domain = get_domain(D1, D2, k_grams, each_hash_q)
    a_sign = get_min_hash_signature(my_domain, split_char(k_grams, D1))
    b_sign = get_min_hash_signature(my_domain, split_char(k_grams, D2))


