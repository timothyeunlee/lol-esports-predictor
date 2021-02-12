import pandas as pd 
import os

# SCRIPT to extract team match data from oracleexlir csvs 
# Patch after elemental dragons (2020 - CURRENT)
#  
def all_teams_stats(): 
    all_teams = [
        '100 Thieves', 
        'Cloud9',
        'Counter Logic Gaming',
        'Dignitas', 
        'Evil Geniuses', 
        'FlyQuest',
        'Golden Guardians', 
        'Immortals',
        'Team Liquid',
        'TSM', 
        'Excel Esports',
        'FC Schalke 04 Esports',
        'Fnatic', 
        'G2 Esports', 
        'MAD Lions',
        'Misfits Gaming', 
        'Rogue',
        'Origen', # 2020
        'SK Gaming',
        'Team Vitality',
        'Astralis', 
        'T1', 
        'Gen.G', 
        'KT Rolster', 
        'Afreeca Freecs', 
        'Nongshim RedForce', 
        'Liiv SANDBOX', 
        'Hanwha Life Esports', 
        'Fredit BRION', 
        'DWG KIA', 
        'DRX',
        'DAMWON Gaming', # 2020
        'SANDBOX Gaming', #2020
        'Griffin', #2020
        'SeolHaeOne Prince', #2020
    ]
    # file_path = '../data/raw_data/2020_LoL_esports_match_data_from_OraclesElixir_20210210.csv'
    file_path = '../data/raw_data/2021_LoL_esports_match_data_from_OraclesElixir_20210210.csv'
    df = pd.read_csv(file_path) 
    filter_teams = df['position'] == 'team'
    teams_df = df[filter_teams]
    new_df = teams_df[teams_df['team'].isin(all_teams)]
    print(new_df)

# main method to get teams from current rosters (2021) 
def get_team_stats(): 
    lcs = ['100 Thieves', 'TSM', 'Team Liquid', 'Counter Logic Gaming', 'Golden Guardians', 'Evil Geniuses', 'Cloud9', 'Immortals', 'FlyQuest', 'Dignitas']
    lec = ['SK Gaming', 'Astralis', 'Excel Esports', 'FC Schalke 04 Esports', 'Fnatic', 'G2 Esports', 'MAD Lions', 'Misfits Gaming', 'Rogue', 'Team Vitality'] 
    lck = ['T1', 'Gen.G', 'KT Rolster', 'Afreeca Freecs', 'Nongshim RedForce', 'Liiv SANDBOX', 'Hanwha Life Esports', 'Fredit BRION', 'DWG KIA', 'DRX']

    # TO RUN SCRIPT DOWNLOAD ALL MATCH DATA FILES FROM 
    # https://oracleselixir.com/tools/downloads
    # SAVE IN A DIR '../data/raw_data'
    match_data_path = '../data/raw_data/' 
    csvs = os.listdir(match_data_path) 
    for csv in csvs:
        year = extract_year(csv)
        get_team_stats_helper(csv, lcs, 'lcs', year)
        get_team_stats_helper(csv, lec, 'lec', year)
        get_team_stats_helper(csv, lck, 'lck', year)

def get_team_stats_helper(csv, team_list, region, year): 
    csv_path = '../data/raw_data/' + csv
    df = pd.read_csv(csv_path) 
    teams_filter = df['position'] == 'team' 
    teams_df = df[teams_filter]

    for team in team_list: 
        get_team = teams_df['team'] == team 
        team_df = teams_df[get_team]
        export_df (team_df, team, region, year)

def export_df(team_df, team, region, year):
    # output_dir = '../data/team_stats_csv'
    output_dir = '../data/2020_2021_team_stats_csv'
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

# def test(): 
#     lck = ['T1', 'Gen.G', 'KT Rolster', 'Afreeca Freecs', 'Nongshim RedForce', 'Liiv SANDBOX', 'Hanwha Life Esports', 'Fredit BRION', 'DWG KIA', 'DRX']
#     match_data_path = '../data/raw_data/2021_LoL_esports_match_data_from_OraclesElixir_20210210.csv'
#     df = pd.read_csv(match_data_path)
#     teams_filter = df['position'] == 'team'
#     teams_df = df[teams_filter] 
#     for team in lck: 
#         get_team = teams_df['team'] == team 
#         team_df = teams_df[get_team]
#         export_df (team_df, team, 'lck', '2021')


def main(): 
    all_teams_stats()
    # get_team_stats()
    # test() 

if __name__ == "__main__": 
    main() 