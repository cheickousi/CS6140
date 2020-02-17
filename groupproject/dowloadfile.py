import requests

# The direct link to the Kaggle data set
data_url = 'https://www.kaggle.com/drgilermo/nba-players-stats#Seasons_Stats.csv'

# The local path where the data set is saved.
local_filename = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/Seasons_Stats.csv"

# Kaggle Username and Password
kaggle_info = {'UserName': "cheick.sissoko@gmail.com", 'Password': "oumar1985"}

# Attempts to download the CSV file. Gets rejected because we are not logged in.
r = requests.get(data_url)

# Login to Kaggle and retrieve the data.
r = requests.post(r.url, data = kaggle_info)

# Writes the data to a local file one chunk at a time.
f = open(local_filename, 'w')
for chunk in r.content: # Reads 512KB at a time into memory
    if chunk: # filter out keep-alive new chunks
        f.write(chunk)
f.close()