import sqlite3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

pd.set_option('display.expand_frame_repr', False)


def getMisraGries(Data, k_1):
    counter_m = 0
    Labels = np.empty(shape=k_1, dtype=np.dtype('U25'))
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


directory = "/Users/CheickSissoko/Documents/SQLite/"
local_filename = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/first_draft_injuries.csv"

conn = create_connection('/Users/CheickSissoko/Documents/SQLite/nba_injuries.db3')

sql = 'SELECT TYPE_OF_INJURY_CLEANSED as words FROM INJURY_DATA2 where TYPE_OF_INJURY_CLEANSED is not null'

injuryBagWords = pd.read_sql(sql=sql, con=conn)
bagWords = []
for idx, each_row in injuryBagWords.iterrows():
    wordString = str(each_row.loc['words']).strip()
    if wordString.__contains__("injury"):
        wordString = wordString.strip().replace(" ", "_")
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
        bagWords.append(first_two_words.strip())
        bagWords.append(next_two_words.strip())
    else:
        first_two_words = " ".join(wordString.split(" ")[:2])
        if len(first_two_words.strip()) > 0:
            bagWords.append(first_two_words.strip())

k = 150
labels, counters, counter_ration = getMisraGries(bagWords, k)
rlabels = pd.DataFrame(labels, columns=['Counter'])
rCounters = pd.DataFrame(counters, columns=['Label'])
rRatio = pd.DataFrame(counter_ration, columns=['Counter_ratio'])
rep = pd.concat([rlabels, rCounters, rRatio], axis=1)

final_report = rep[rep['Counter_ratio'] > 1].sort_values(by=['Counter_ratio'])

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(final_report["Label"], final_report["Counter_ratio"])
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlabel='Ratio/Percentage', ylabel='Injury Type',
       title='Misra Gries Most frequent Injuries')

plt.show()
