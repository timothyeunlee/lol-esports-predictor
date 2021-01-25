import os
import requests
import itertools
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint

lcs = ['100_Thieves', 'TSM', 'Team_Liquid', 'Counter_Logic_Gaming', 'Golden_Guardians', 'Evil_Geniuses', 'Cloud9', 'Immortals', 'FlyQuest', 'Dignitas']
lec = ['SK_Gaming', 'Astralis', 'Excel_Esports', 'FC_Schalke_04_Esports', 'Fnatic', 'G2_Esports', 'MAD_Lions', 'Misfits_Gaming', 'Rogue_(European_Team)', 'Team_Vitality'] 
lck = ['T1', 'Gen.G', 'KT_Rolster', 'Afreeca_Freecs', 'Nongshim_RedForce', 'Liiv_SANDBOX', 'Hanwha_Life_Esports', 'Fredit_BRION', 'DWG_KIA', 'DRX']

lcs_teams = {}
lec_teams = {}
lck_teams = {}

# builds inital dictionary of teams 
def make_team_dict(): 
    for team_name in lcs: 
        lcs_teams[team_name] = {}

    for team_name in lec: 
        lec_teams[team_name] = {}
    
    for team_name in lck: 
        lck_teams[team_name] = {}

def fill_dictionary(): 
    for team in lcs: 
        url = 'https://lol.gamepedia.com/' + team
        scrape_team_roster(url, team, lcs_teams)
    
    for team in lec:
        url = 'https://lol.gamepedia.com/' + team
        scrape_team_roster(url, team, lec_teams)

    for team in lck:
        url = 'https://lol.gamepedia.com/' + team
        scrape_team_roster(url, team, lck_teams)

    # test('https://lol.gamepedia.com/T1', 'T1', lck_teams)

# specific input params
# 'https://lol.gamepedia.com/T1', 'T1', lck_teams(dictionary) 
def scrape_team_roster(teamUrl, team, dict): 
    page = requests.get(teamUrl)

    soup = BeautifulSoup(page.content, 'html.parser')

    # get CURRENT roster for teams 
    current_roster = soup.find('table', {'class': 'team-members-current'})
    player = current_roster.find_all('td', {'class': 'team-members-player'}) 
    role = current_roster.find_all('td', {'class': 'team-members-role'})

    for td1, td2 in itertools.zip_longest(player, role): 
        summoner_name = td1.text 
        player_role = td2.text 
        dict[team][summoner_name] = player_role

def export_csv(): 
    lcs_output_file = 'lcs_player_roster.csv'
    lec_output_file = 'lec_player_roster.csv' 
    lck_output_file = 'lck_player_roster.csv' 

    output_dir = './player_roster_csv' 
    
    if not os.path.exists(output_dir): 
        os.mkdir(output_dir) 

    lcs_fullpath = os.path.join(output_dir, lcs_output_file)
    lec_fullpath = os.path.join(output_dir, lec_output_file)
    lck_fullpath = os.path.join(output_dir, lck_output_file)

    pd.DataFrame.from_dict(lcs_teams, orient='index').to_csv(lcs_fullpath)
    pd.DataFrame.from_dict(lec_teams, orient='index').to_csv(lec_fullpath)
    pd.DataFrame.from_dict(lck_teams, orient='index').to_csv(lck_fullpath)

def test(teamUrl, team, dict):
    page = requests.get(teamUrl)

    soup = BeautifulSoup(page.content, 'html.parser')

    # get CURRENT roster for teams 
    current_roster = soup.find('table', {'class': 'team-members-current'})
    player = current_roster.find_all('td', {'class': 'team-members-player'}) 
    role = current_roster.find_all('td', {'class': 'team-members-role'})

    for td1, td2 in itertools.zip_longest(player, role, fillvalue=''): 
        summoner_name = td1.text 
        player_role = td2.text 
        dict[team][summoner_name] = player_role

if __name__ == "__main__":
    make_team_dict()
    fill_dictionary()
    export_csv()


# outname = 'name.csv'

# outdir = './dir'
# if not os.path.exists(outdir):
#     os.mkdir(outdir)

# fullname = os.path.join(outdir, outname)    

# df.to_csv(fullname)