import sqlite3
from collections import Counter

import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

pd.set_option('display.expand_frame_repr', False)


def create_connection(db_file):
    """ create a database connection to the SQLite database
           specified by db_file
       :param db_file: database file
       :return: Connection object or None
       """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


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


directory = "/Users/CheickSissoko/Documents/SQLite/"
local_filename = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/first_draft_injuries.csv"
path_X = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/X.csv"
path_y = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/Y.csv"
conn = create_connection('/Users/CheickSissoko/Documents/SQLite/nba_injuries.db3')
sql = 'SELECT *  FROM INJURY_DATA2 where TYPE_OF_INJURY_CLEANSED is not null and GAMES_PLAYED is not null'

injuryBagWords = pd.read_sql(sql=sql, con=conn)
bagWords = []
for idx, each_row in injuryBagWords.iterrows():
    # converting height to inches
    height = str(each_row.loc['HEIGHT']).strip()
    H_feet = height.split("-")[0]
    H_inch = height.split("-")[1]
    H_inches = int(H_feet) * 12 + int(H_inch)
    injuryBagWords.loc[idx, 'HEIGHT'] = H_inches
    wordString = str(each_row.loc['TYPE_OF_INJURY_CLEANSED']).strip()

    # CLEANSING AND CONDENSING TYPE OF INJURY
    if wordString.__contains__("in"):
        wordString = wordString.replace(' in ', '')
    if wordString.__contains__("partially"):
        wordString = wordString.replace('partially ', '')
    if wordString.__contains__("(P)"):
        wordString = wordString.replace('(P) ', '')
        wordString = wordString.replace('(P)', '')
    if wordString.__contains__("(CBC)"):
        wordString = wordString.replace('(CBC)', '')
        if wordString.__contains__("left"):
            wordString = wordString.replace(' left ', '')
    if wordString.__contains__("/"):
        ListWord = wordString.split("/")
        first_two_words = ListWord[0]
        next_two_words = ListWord[1]
        injuryBagWords.loc[idx, 'TYPE_OF_INJURY_CLEANSED'] = first_two_words
        bagWords.append(first_two_words.strip())
        bagWords.append(next_two_words.strip())
    else:
        first_two_words = " ".join(wordString.split(" ")[:2])
        if len(first_two_words.strip()) > 0:
            bagWords.append(first_two_words.strip())
            injuryBagWords.loc[idx, 'TYPE_OF_INJURY_CLEANSED'] = first_two_words

injuryBagWords = injuryBagWords[injuryBagWords['TYPE_OF_INJURY_CLEANSED'] != '']
cols_with_integers = ['MONTH', 'AGE', 'GAMES_PLAYED', 'MINUTES_PLAYED',
                      'PLAYER_EFFICIENCY_RATING', 'POINTS_SCORED', 'FIELD_GOALD',
                      'BODY_LOCATION', 'POSITION', 'REQUIRED_SURGERY', 'HEIGHT', 'TYPE_OF_INJURY_CLEANSED']
cols_with_text = ['BODY_LOCATION', 'POSITION', 'TYPE_OF_INJURY_CLEANSED', 'REQUIRED_SURGERY']

# CONVERTING COLUMNS WITH STRING VALUE INTO FLOATS
for each_col in cols_with_text:
    arrayData = ordinal_encode(injuryBagWords[each_col])
    injuryBagWords[each_col] = arrayData

cols_X = ['MONTH', 'AGE', 'MINUTES_PLAYED',
          'PLAYER_EFFICIENCY_RATING', 'POINTS_SCORED', 'FIELD_GOALD',
          'BODY_LOCATION', 'POSITION', 'REQUIRED_SURGERY', 'HEIGHT', 'TYPE_OF_INJURY_CLEANSED']

cols_y = ['GAMES_PLAYED']
injuryBagWords[cols_X].to_csv(path_or_buf=path_X, header=False)
injuryBagWords[cols_y].to_csv(path_or_buf=path_y, header=False)
