import numpy as np
import pandas as pd
import string
from itertools import combinations
import re
from string import punctuation

st = "some test firlew tring to be creat bag of words and be aagin "


def split_word(string):
    words = re.split('\s', string.rstrip())
    return list(map(' '.join, zip(words[:-1], words[1:])))


def split_char(k_grams, string):
    string = remove_all_punctuation(string)
    my_out = np.unique([(string[i:i + k_grams]) for i in range(0, len(string), k_grams)])
    return my_out


def remove_all_punctuation(string):
    return "".join((char for char in string.rstrip() if char not in punctuation))


#


input_directory = "//Users/CheickSissoko/Documents/Spring2020_CS6140/implementations/hw2/"


def get_text(doc_name):
    file = open(input_directory + doc_name + ".txt", "r")
    text = file.readline()
    file.close()
    return text


def get_jaccar_sim(di_kgram, dj_kgram):
    intersect = np.size(np.intersect1d(dj_kgram, di_kgram))
    union = np.size(np.union1d(di_kgram, dj_kgram))
    return intersect / union


k_grams_character = [2, 3]
k_grams_words = 2

mylist = ["D1", "D2", "D3", "D4"]
list_of_pairs = list(combinations(mylist,2))
print(res)