import pandas as pd 
import os 
from os import listdir
from os.path import isfile, join

# path = './player_roster_csv/lck_player_roster'
path = '/Users/timothylee/lol-esports-predictor/src/player_roster_csv/lck_player_roster.csv'
df = pd.read_csv(path)
df = df.drop(df.columns[0], axis = 1)
players = df.columns.tolist()
print(players)