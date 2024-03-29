import sqlite3

import pandas as pd

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


directory = "/Users/CheickSissoko/Documents/SQLite/"
local_filename = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/first_draft_injuries.csv"

conn = create_connection('/Users/CheickSissoko/Documents/SQLite/nba_injuries.db3')

# sql = 'SELECT * FROM INJURY_DATA2 '
# excel = pd.read_sql(sql=sql, con=conn)

# excel.to_csv(path_or_buf="/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/consolidateData_v2.csv")


# print(excel['TYPE_OF_INJURY_CLEANSED'].head(103))

sql = 'SELECT *  FROM INJURY_DATA2 where TYPE_OF_INJURY_CLEANSED is not null'

injuryBagWords = pd.read_sql(sql=sql, con=conn)
bagWords = []
for idx, each_row in injuryBagWords.iterrows():
    wordString = str(each_row.loc['TYPE_OF_INJURY_CLEANSED']).strip()
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
        each_row.loc[idx, 'TYPE_OF_INJURY_CLEANSED'] = first_two_words
        bagWords.append(first_two_words.strip())
        bagWords.append(next_two_words.strip())
    else:
        first_two_words = " ".join(wordString.split(" ")[:2])
        if len(first_two_words.strip()) > 0:
            bagWords.append(first_two_words.strip())
            each_row.loc[idx, 'TYPE_OF_INJURY_CLEANSED'] = first_two_words

print(injuryBagWords['TYPE_OF_INJURY_CLEANSED'])
