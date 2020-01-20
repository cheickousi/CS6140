import numpy as np
import string
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


print(split_char(2, st))
