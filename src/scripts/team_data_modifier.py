"""
    Script to do various changes to team data 
    - make changes for various ml models
    - make averages for team's etc.
"""
import scripts_helper_functions as helper
import os
import pandas as pd 

def team_averages(): 
    drop_cols = ['Unnamed: 0.1', 'Unnamed: 0']
    team_stats_csv = '../data/team_data/2020_2021_team_stats.csv'
    df = pd.read_csv(team_stats_csv)
    team_stats = df.drop(drop_cols, axis = 1)
    team_df = team_stats.groupby(team_stats.team)
    means = team_df.mean()
    helper.df_export(means, '../data/team_averages', 'team_averages.csv')     

def main(): 
    team_averages()

if __name__ == "__main__":
    main()