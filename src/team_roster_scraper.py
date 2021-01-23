import requests
import itertools
from bs4 import BeautifulSoup
from pprint import pprint

lcs = ['100_Thieves', 'TSM', 'Team_Liquid', 'Counter_Logic_Gaming', 'Golden_Guardians', 'Evil_Geniuses', 'Cloud9', 'Immortals', 'FlyQuest', 'Dignitas']
lec = ['SK_Gaming', 'Astralis', 'Excel_Esports', 'FC_Schalke_04_Esports', 'Fnatic', 'G2_Esports', 'MAD_Lions', 'Misfits_Gaming', 'Rogue_(European_Team)', 'Team_Vitality'] 
lck = ['T1', 'Gen.G', 'KT_Rolster', 'Afreeca_Freecs', 'Nongshim_RedForce', 'Liiv_SANDBOX', 'Hanwha_Life_Esports', 'Fredit_BRION', 'DWG_KIA', 'DRX']

lcs_teams = {}
lec_teams = {}
lck_teams = {}

# specific input params
# 'https://lol.gamepedia.com/T1', 'T1', lck_teams(dictionary) 
def scrape_team_roster(teamUrl, team, dict): 
    page = requests.get(teamUrl)

    soup = BeautifulSoup(page.content, 'html.parser')

    # get CURRENT roster for teams 
    current_roster = soup.find('table', {'class': 'team-members-current'})
    player = current_roster.find_all('td', {'class': 'team-members-player'}) 
    role = current_roster.find_all('td', {'class': 'team-members-role'})

    for td1, td2 in zip(player, role): 
        summoner_name = td1.text 
        player_role = td2.text 
        dict[team][summoner_name] = player_role

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

def export_csv(): 
    return 0

def test(teamUrl, team, dict):
    page = requests.get(teamUrl)

    soup = BeautifulSoup(page.content, 'html.parser')

    # get CURRENT roster for teams 
    current_roster = soup.find('table', {'class': 'team-members-current'})
    player = current_roster.find_all('td', {'class': 'team-members-player'}) 
    role = current_roster.find_all('td', {'class': 'team-members-role'})

    # print ('player ', len(player)) 
    # print ('role: ', len(role))
    for td1, td2 in itertools.zip_longest(player, role, fillvalue=''): 
        summoner_name = td1.text 
        player_role = td2.text 
        # print(summoner_name)
        # print(player_role)
        dict[team][summoner_name] = player_role

if __name__ == "__main__":
    make_team_dict()
    fill_dictionary()
    # print(lcs_teams)
    # print(lec_teams)
    # print(lck_teams['T1']) 