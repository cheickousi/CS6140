import pandas as pd
import os

directory = "/Users/CheickSissoko/Documents/Spring2020_CS6140/groupproject/"

injuries = pd.read_csv(directory + 'injuries.csv - Sheet1.csv')
player_data = pd.read_csv(directory + 'player_data.csv - Sheet1.csv')
players = pd.read_csv(directory + 'Players.csv - Sheet1.csv')

# seasons = pd.read_csv(directory + 'Seasons_Stats.csv')

print(injuries.shape)
print(players.shape)
print(player_data.shape)

print(injuries.keys())
print(players.keys())
print(player_data.keys())
