import os 
import requests
import pprint
import pandas as pd
from bs4 import BeautifulSoup

# SCRIPT PROCESS 
# player_stats 
    # - iterate through player roster,
    # - for each player in specific team, 
    # - send each player to (scrape_player_stats_by_year)
# scrape_player_stats_by_year
#   - use beautiful soup to scrape webpage 
#   - there are 16 stat for each champion player has played
#   - for each 16 stats send to (fill_player_champion_stats) 
# fill_player_champion_stats
#     - (fill_player_champion_stats) will loop through each of the stats and populate a temporary dictionary 
#             - and return it to scrape_player_stats_by_year
#     - scrape_player_stats_by_year will then update the players dictionary 

tournament_set = set()

def player_stats(year):
    # need to import csv and get player data keys 
    sample_player_dict = {
        'T1': {'Faker': 'Mid', 'Teddy': 'Bot', 'Canna': 'Jungler'}, 'DWG': {'ShowMaker': 'Mid', 'Khan': 'Top'} 
        # 'T1': {'Faker': 'Mid'}, 'DWG': {'ShowMaker': 'Mid'}
        # 'T1': {'Faker': 'Mid'}
    }

    player_dict = {} 
    for team in sample_player_dict.keys():
        player_dict[team] = {}
        for player in sample_player_dict[team].keys():
            player_dict[team][player] = {} 
            scrape_player_stats_by_year(team, player, player_dict, year)

    export_csv(player_dict)
    # pprint.pprint(player_dict)

def scrape_player_stats_by_year(team, player, player_dict, year):  
    player_url = 'https://lol.gamepedia.com/' + player + '/Statistics/' + year

    # faker_url = 'https://lol.gamepedia.com/Faker/Statistics/2021' 

    page = requests.get(player_url) 

    soup = BeautifulSoup(page.content, 'html.parser')

    page_div = soup.find('div', {'class': 'mw-parser-output'})
    tournament_div = page_div.find_all('div', {'class': 'wide-content-scroll'})

    stat_list = []
    for tag in tournament_div: 
        tournament_name = tag.find('a', {'class': 'mw-redirect to_hasTooltip'})
        
        tournament_set.add(tournament_name.text)

        player_dict[team][player][tournament_name.text] = {}
        count = 0
        stats = tag.find_all('td')

        for stat in stats:
            stat_list.append(stat.text) 
            count += 1
            if count == 16:
                champion_dict = fill_player_champion_stats(stat_list)
                player_dict[team][player][tournament_name.text].update(champion_dict)

                stat_list.clear()
                count = 0  

def fill_player_champion_stats(stat_list):
    temp_dict = {}
    temp_dict[stat_list[0]] = {}

    for count, stat in enumerate(stat_list[1:16]):
        temp_dict[stat_list[0]][check_index(count)] = stat
    
    return temp_dict

def check_index(index): 
    item = index % 15
    mapping = { 
        0: 'Games',
        1: 'Win',
        2: 'Loss',
        3: 'W/L Ratio',
        4: 'Kill',
        5: 'Death',
        6: 'Assist',
        7: 'KDA',
        8: 'CS',
        9: 'CS/M',
        10: 'Gold',
        11: 'Gold/M',
        12: 'Kill Participation',
        13: 'Kill Share',
        14: 'Gold Share',
    }

    return mapping.get(item)

def export_csv(player_stats): 
    lck_output_file = 'lck_player_stats.csv'

    output_dir = './player_stats_csv'

    if not os.path.exists(output_dir): 
        os.mkdir(output_dir)
    
    lck_fullpath = os.path.join(output_dir, lck_output_file)

    pd.DataFrame.from_dict(player_stats, orient='index').to_csv(lck_fullpath)

if __name__ == "__main__":
    player_stats('2020')