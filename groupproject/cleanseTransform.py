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


conn = create_connection('/Users/CheickSissoko/Documents/SQLite/nba_injuries.db3')
out_filename = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/"
injury_sql = 'SELECT * FROM INJURY_DATA WHERE PLAYER_EFFICIENCY_RATING IS NOT NULL'
surgery_sql = 'SELECT *  FROM surgeries'
injury = pd.read_sql(sql=injury_sql, con=conn)
surgeries = pd.read_sql(sql=surgery_sql, con=conn)

# print(surgeries.head(10))

column_year = 'YEAR'
column_month = 'MONTH'
column_team = 'Team'
column_name = 'PLAYER_NAME'
column_note = 'Notes'
column_required_surgery = 'REQUIRED_SURGERY'

result = []
for row, value in injury.iterrows():
    for row2, value2 in surgeries.iterrows():
        key = str(value[column_name]) + str(value[column_month]) + str(value[column_year]) + str(value[column_team])
        key2 = str(value2[column_name]) + str(value2[column_month]) + str(value2[column_year]) + str(
            value2[column_team])
        if key == key2:
            result.append(True)
        else:
            result.append(False)

injury[column_required_surgery] = result
injury.to_csv(path_or_buf=out_filename + "second" + "DraftInjuries.csv")
print("Done")
