import os 
from os import listdir
from os.path import isfile, join

import requests
import pprint
import pandas as pd
from bs4 import BeautifulSoup

tournament_set = set()
players_with_no_stats = [] 

def player_stats(year, players, region):
    player_dict = {}
    player_dict[region] = {} 

    for player in players:
        player_dict[region][player] = {}
        scrape_player_stats_by_year(player, player_dict, year, region)
        export_csv(player_dict, region)
        
    # export_csv(player_dict)
    # pprint.pprint(player_dict)

def scrape_player_stats_by_year(player, player_dict, year, region):  
    player_url = 'https://lol.gamepedia.com/' + player + '/Statistics/' + year

    page = requests.get(player_url)

    soup = BeautifulSoup(page.content, 'html.parser')

    try: 
        page_div = soup.find('div', {'class': 'mw-parser-output'})
        tournament_div = page_div.find_all('div', {'class': 'wide-content-scroll'})

        stat_list = []
        for tag in tournament_div: 
            tournament_name = tag.find('a', {'class': 'mw-redirect to_hasTooltip'})
            tournament_set.add(tournament_name.text)
            player_dict[region][player][tournament_name.text] = {}
            stats = tag.find_all('td')

            count = 0
            for stat in stats:
                stat_list.append(stat.text) 
                count += 1
                if count == 16:
                    champion_dict = fill_player_champion_stats(stat_list)
                    player_dict[region][player][tournament_name.text].update(champion_dict)
                    stat_list.clear()
                    count = 0  
    except AttributeError:
        pass
    
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

def read_roster_csv(year): 
    roster_directory = './player_roster_csv'
    csvs = os.listdir(roster_directory) 

    for csv in csvs: 
        region = extract_region_path(csv)
        csv_path = roster_directory + '/' + csv
        df = pd.read_csv(csv_path)
        df = df.drop(df.columns[0], axis = 1)
        players = df.columns.tolist()
        player_stats(year, players, region)

def export_csv(player_stats, region): 
    output_file = region.lower() + '_player_stats.csv'
    output_dir = './player_stats_csv'

    if not os.path.exists(output_dir): 
        os.mkdir(output_dir)

    fullpath = os.path.join(output_dir, output_file)
    pd.DataFrame.from_dict(player_stats, orient='index').to_csv(fullpath)

def extract_region_path(path):
    modified_path = path[:3].upper()
    return modified_path

if __name__ == "__main__":
    read_roster_csv('2020') 