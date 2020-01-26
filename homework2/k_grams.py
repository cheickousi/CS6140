import os
import numpy as np
from string import punctuation
from itertools import combinations
import pandas as pd
import re

from homework2.inputs import D1, D2, D3, D4


def split_char(k_grams, string):
    string = remove_all_punctuation(string)
    my_out = np.unique([(string[i:i + k_grams]) for i in range(len(string) + 1 - k_grams) ])
    return my_out


def split_word(string):
    words = re.split('\s', remove_all_punctuation(string.rstrip()))
    return np.unique(list(map(' '.join, zip(words[:-1], words[1:]))))


def remove_all_punctuation(string):
    return "".join((char for char in string if char not in punctuation))


def get_jaccar_sim(di_kgram, dj_kgram):
    intersect = np.size(np.intersect1d(dj_kgram, di_kgram))
    union = np.size(np.union1d(di_kgram, dj_kgram))
    return intersect / union


printList = ["D1", "D2", "D3", "D4"]
myList = [D1, D2, D3, D4]
k_grams_character = [2, 3]
k_grams_words = 2

columns = ["document", "k-grams", "unique_count"]
result = pd.DataFrame([], columns=columns)

for each_d, print_d in zip(myList, printList):
    i = 1
    for each_kc in k_grams_character:
        char_grams = split_char(each_kc, each_d)
        const = "G" + str(i)
        out = pd.DataFrame([[print_d, const, len(char_grams)]], columns=columns)
        result = result.append(out)
        i += 1
    word_grams = split_word(each_d)
    out2 = pd.DataFrame([[print_d, "G3", len(word_grams)]], columns=columns)
    result = result.append(out2)

print("A: (25 points) How many distinct k-grams are there for each document with each type of k-gram?", "\n")
print(result, "\n")

print("B: (25 points) Compute the Jaccard similarity between all pairs of documents for each type of k-gram.", "\n")

printList = ["D1", "D2", "D3", "D4"]
columns_2 = ["Sets", "k-grams_Constructor", "Jaccard Similarity"]
result = pd.DataFrame([], columns=columns_2)
list_of_pairs = list(combinations(myList, 2))
print_pairs = list(combinations(printList, 2))
j = 1

for each_pair, print_d in zip(list_of_pairs, print_pairs):
    i_text = each_pair[0]
    j_text = each_pair[1]
    i = 1
    for each_kc in k_grams_character:
        char_grams_j = split_char(each_kc, i_text)
        char_grams_i = split_char(each_kc, j_text)
        jacc = get_jaccar_sim(char_grams_i, char_grams_j)
        const = "G" + str(i)
        out = pd.DataFrame([[print_d, const, jacc]], columns=columns_2)
        result = result.append(out)
        i += 1
    word_grams_i = split_word(i_text)
    word_grams_j = split_word(j_text)
    jacc_2 = get_jaccar_sim(word_grams_i, word_grams_j)
    out2 = pd.DataFrame([[print_d, "G3", jacc_2]], columns=columns_2)
    result = result.append(out2)

print(result, "\n")
