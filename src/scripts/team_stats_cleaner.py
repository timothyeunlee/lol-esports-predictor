import os
import pandas as pd 

"""
    SCRIPT to do various cleaning tasks to team filtered data 
"""
# combine files from '2020_2021_team_stats_csv' into a single csv
# use case to easily manipulate ceratin features for ml models  
def unfiltered_features_csv_maker(): 
    csvs_path = '../data/2020_2021_raw_team_stats_csv'
    csvs = os.listdir(csvs_path)
    frames = [] 
    for csv in csvs: 
        full_csv_path = csvs_path + '/' + csv
        df = pd.read_csv(full_csv_path) 
        frames.append(df) 
    combined_df = pd.concat(frames) 
    export(combined_df) 

# iterates through all csvs in directory 
# drops columns, concats them together, exports 
def clean_csv(): 
    csvs_path = '../data/2020_2021_raw_team_stats_csv'
    csvs = os.listdir(csvs_path)
    frames = [] # list of every data frame in the csv dir 
    for csv in csvs: 
        full_csv_path = csvs_path + '/' + csv
        df = pd.read_csv(full_csv_path) 
        dropped_df = drop_columns(df)
        frames.append(dropped_df)
    combined_df = pd.concat(frames)
    export(combined_df)

# drops unncessary columns 
# returns new df 
def drop_columns(df):
    new_df = df[['result', 'kills', 'deaths', 'dragons', 'elders', 'heralds', 'barons', 'goldat15', 'golddiffat15']]
    return new_df

def export(df): 
    output_dir = '../data/teams_ml_data'
    output_file = 'combined_team_stats.csv'
    
    if not os.path.exists(output_dir): 
        os.mkdir(output_dir) 

    complete_path = os.path.join(output_dir, output_file) 
    df.to_csv(complete_path) 

def main():
    # clean_csv() 
    unfiltered_features_csv_maker()

if __name__ == "__main__": 
    main()