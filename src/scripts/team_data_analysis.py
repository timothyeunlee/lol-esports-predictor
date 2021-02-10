import pandas as pd 
import os

def get_team_stats(): 
    lcs = ['100 Thieves', 'TSM', 'Team Liquid', 'Counter Logic Gaming', 'Golden Guardians', 'Evil Geniuses', 'Cloud9', 'Immortals', 'FlyQuest', 'Dignitas']
    lec = ['SK Gaming', 'Astralis', 'Excel Esports', 'FC Schalke 04 Esports', 'Fnatic', 'G2 Esports', 'MAD Lions', 'Misfits Gaming', 'Rogue', 'Team Vitality'] 
    lck = ['T1', 'Gen.G', 'KT Rolster', 'Afreeca Freecs', 'Nongshim RedForce', 'Liiv SANDBOX', 'Hanwha Life Esports', 'Fredit BRION', 'DWG KIA', 'DRX']

    # TO RUN SCRIPT DOWNLOAD ALL MATCH DATA FILES FROM 
    # https://oracleselixir.com/tools/downloads
    # SAVE IN A DIR 'match_data_csv/'
    match_data_path = './match_data_csv' 
    csvs = os.listdir(match_data_path) 
    for csv in csvs:
        year = extract_year(csv)
        get_team_stats_helper(csv, lcs, 'lcs', year)
        get_team_stats_helper(csv, lec, 'lec', year)
        get_team_stats_helper(csv, lck, 'lck', year)

def get_team_stats_helper(csv, team_list, region, year): 
    csv_path = './match_data_csv/' + csv
    df = pd.read_csv(csv_path) 
    teams_filter = df['position'] == 'team' 
    teams_df = df[teams_filter]

    for team in team_list: 
        get_team = teams_df['team'] == team 
        team_df = teams_df[get_team]
        export_df (team_df, team, region, year)

def export_df(team_df, team, region, year):
    output_dir = './data/team_stats_csv'
    year_dir = output_dir + '/' + year
    region_dir = year_dir + '/' + region 
    formatted_team = format_team(team)
    output_file = formatted_team + '_stats.csv' 

    if not os.path.exists(output_dir): 
        os.mkdir(output_dir)
    if not os.path.exists(year_dir): 
        os.mkdir(year_dir)
    if not os.path.exists(region_dir): 
        os.mkdir(region_dir) 

    complete_path = os.path.join (region_dir, output_file) 
    # print(team_df.shape)
    team_df.to_csv(complete_path)

def format_team(team_name): 
    return team_name.replace(' ', '_').lower()

def extract_year(csv_file):
    return csv_file[:4]

def main(): 
    get_team_stats()

if __name__ == "__main__": 
    main() 