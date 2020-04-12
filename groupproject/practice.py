from collections import Counter

import numpy as np
from sklearn.preprocessing import OrdinalEncoder


def ordinal_encode(a_column_of_dataframe):
    # make an array of unique categories by count for preference, because apparently the most occurred is what most
    # offered(in context of hotel rooms)
    most_occurred_desc = np.array(
        sorted(a_column_of_dataframe.values, key=Counter(a_column_of_dataframe.values).get, reverse=True))
    unique_elements = list(Counter(most_occurred_desc).keys())
    # make an ordinal encoder with that ordered list
    prop_ord_enc = OrdinalEncoder(categories=[unique_elements])
    # since transform needs list of lists
    list_of_lists = [[i] for i in list(a_column_of_dataframe)]
    # transform it now(ordinal encode it), which will return list of lists, just as been passed
    encoded_props = prop_ord_enc.fit_transform(list_of_lists)
    # return the flattened array
    return np.asarray(encoded_props)


path = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/matrices.csv"

# U, s, Vt = LA.svd(sparse, full_matrices=False)
