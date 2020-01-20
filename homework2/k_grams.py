import os
import numpy as np
from string import punctuation
from itertools import combinations
import pandas as pd
import re

input_directory = "//Users/CheickSissoko/Documents/Spring2020_CS6140/implementations/hw2/"


def split_char(k_grams, string):
    string = remove_all_punctuation(string)
    my_out = np.unique([(string[i:i + k_grams]) for i in range(0, len(string), k_grams)])
    return my_out


def split_word(string):
    words = re.split('\s', remove_all_punctuation(string.rstrip()))
    return np.unique(list(map(' '.join, zip(words[:-1], words[1:]))))


def remove_all_punctuation(string):
    return "".join((char for char in string.rstrip() if char not in punctuation))


def get_text(doc_name):
    file = open(input_directory + doc_name + ".txt", "r")
    text = file.readline()
    file.close()
    return text


def get_jaccar_sim(di_kgram, dj_kgram):
    intersect = np.size(np.intersect1d(dj_kgram, di_kgram))
    union = np.size(np.union1d(di_kgram, dj_kgram))
    return intersect / union


#
# for filename in os.listdir(input_directory):
#     with open(input_directory + filename, "r") as fp:
#         print(fp.readline())
#         fp.close()

k_grams_character = [2, 3]
k_grams_words = 2

columns = ["document", "k-grams_Constructor", "unique_k-gram_count"]
result = pd.DataFrame([], columns=columns)

for filename in os.listdir(input_directory):
    with open(input_directory + filename, "r") as fp:
        lines = fp.readline()
        for each_kc in k_grams_character:
            char_grams = split_char(each_kc, lines)
            const = str(each_kc) + "-grams characters"
            out = pd.DataFrame([[filename, const, char_grams.__len__()]], columns=columns)
            result = result.append(out)
        word_grams = split_word(lines)
        out2 = pd.DataFrame([[filename, "2-grams words", len(word_grams)]], columns=columns)
        result = result.append(out2)
        fp.close()

print("A: (25 points) How many distinct k-grams are there for each document with each type of k-gram?", "\n")
print(result, "\n")

print("B: (25 points) Compute the Jaccard similarity between all pairs of documents for each type of k-gram.", "\n")
mylist = ["D1", "D2", "D3", "D4"]

columns_2 = ["Sets", "k-grams_Constructor", "Jaccard Similarity"]
result = pd.DataFrame([], columns=columns_2)
list_of_pairs = list(combinations(mylist,2))
for each_pair in list_of_pairs:
    i_text = get_text(each_pair[0])
    j_text = get_text(each_pair[1])
    for each_kc in k_grams_character:
        char_grams_j = split_char(each_kc, i_text)
        char_grams_i = split_char(each_kc, j_text)
        jacc = get_jaccar_sim(char_grams_i, char_grams_j)
        const = str(each_kc) + "-grams characters"
        out = pd.DataFrame([[each_pair, const, jacc]], columns=columns_2)
        result = result.append(out)
    word_grams_i = split_word(i_text)
    word_grams_j = split_word(j_text)
    jacc_2 = get_jaccar_sim(word_grams_i, word_grams_j)
    out2 = pd.DataFrame([[each_pair, "2-grams words", jacc_2]], columns=columns_2)
    result = result.append(out2)

print(result, "\n")
