import os
import numpy as np
from string import punctuation
import pandas as pd
import re


def split_char(k_grams, string):
    string = remove_all_punctuation(string)
    my_out = np.unique([(string[i:i + k_grams]) for i in range(0, len(string), k_grams)])
    return my_out


def split_word(string):
    words = re.split('\s', remove_all_punctuation(string.rstrip()))
    return np.unique(list(map(' '.join, zip(words[:-1], words[1:]))))


def remove_all_punctuation(string):
    return "".join((char for char in string.rstrip() if char not in punctuation))


input_directory = "//Users/CheickSissoko/Documents/Spring2020_CS6140/implementations/hw2/"
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
        result= result.append(out2)
        fp.close()

print("A: (25 points) How many distinct k-grams are there for each document with each type of k-gram?", "\n")
print(result)

print("B: (25 points) Compute the Jaccard similarity between all pairs of documents for each type of k-gram.")