import sqlite3

import pandas as pd


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

sql = 'SELECT * FROM INJURY_DATA2 '
excel = pd.read_sql(sql=sql, con=conn)

excel.to_csv(path_or_buf="/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/consolidateData_v2.csv")
