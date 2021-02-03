import os 
from os import listdir
from os.path import isfile, join
import requests
import pandas as pd
from bs4 import BeautifulSoup

players_with_no_stats = [] 

def player_stats(year, players, region):
    for player in players:
        player_dict = {}
        scrape_player_stats_by_year(player, player_dict, year)
        export_helper(player_dict, region, player, year)
        
def scrape_player_stats_by_year(player, player_dict, year):  
    player_url = 'https://lol.gamepedia.com/' + player + '/Statistics/' + year

    page = requests.get(player_url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    try: 
        page_div = soup.find('div', {'class': 'mw-parser-output'})
        tournament_div = page_div.find_all('div', {'class': 'wide-content-scroll'})

        stat_list = []
        for tag in tournament_div: 
            tournament_name = tag.find('a', {'class': 'mw-redirect to_hasTooltip'})
            player_dict[tournament_name.text] = {}
            stats = tag.find_all('td')
            count = 0
            for stat in stats:
                stat_list.append(stat.text) 
                count += 1
                if count == 16:
                    champion_dict = fill_player_champion_stats(stat_list)
                    player_dict[tournament_name.text].update(champion_dict)
                    stat_list.clear()
                    count = 0
    except AttributeError:
        players_with_no_stats.append(player)
    
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
        10: 'Gold(k)',
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

def export_csv(player_dict, tournament_name, region, player, year): 
    output_dir = './player_stats_csv/'
    year_dir   = output_dir + '/' + year
    region_dir = year_dir + '/' + region.lower()
    player_dir = region_dir + '/' + player

    formated_name = replace_tournament_name(tournament_name)
    output_file = formated_name + '.csv'

    if not os.path.exists(output_dir): 
        os.mkdir(output_dir)
    if not os.path.exists(year_dir): 
        os.mkdir(year_dir)
    if not os.path.exists(region_dir):
        os.mkdir(region_dir)
    if not os.path.exists(player_dir): 
        os.mkdir(player_dir)

    fullpath = os.path.join(player_dir, output_file)
    pd.DataFrame.from_dict(player_dict, orient='index').to_csv(fullpath)

def export_helper(player_dict, region, player, year):
    temp_dict = player_dict
    for key in temp_dict.keys(): 
        export_csv(temp_dict[key], key, region, player, year)

def replace_tournament_name(tournament_name): 
    formated_name = tournament_name.replace(' ', '_').lower()
    return formated_name

def extract_region_path(path):
    modified_path = path[:3].upper()
    return modified_path

def players_no_stats_by_year(year): 
    directory_path = './player_stats_csv/' + year
    file_name = 'players_with_no_stats_' + year + '.txt'
    complete_path = os.path.join(directory_path, file_name)
    abs_path = os.path.abspath(complete_path)
    with open(abs_path, 'a+') as player_file:
        player_file.write(str(players_with_no_stats))

def test():
    players = ['Canna', 'Zeus', 'Cuzz', 'Ellim', 'Oner', 'Clozer', 'Faker', 'Gumayusi', 'Teddy', 'Keria', 'Burdol', 'Rascal', 'Clid', 'Flawless', 'Bdd', 'Karis', 'Ruler', 'Life', 'Doran', 'Blank', 'Bonnie', 'Dove', 'Ucal', 'HyBriD', 'Zzus', 'Kiin', 'Dread', 'Fly', 'Keine', 'Bang', 'Lehends', 'Rich', 'Juhan', 'Peanut', 'Bay', 'deokdam', 'Wayne', 'Kellin', 'Summit', 'Croco', 'OnFleek', 'FATE', 'Leo', 'Route', 'Effort', 'DuDu', 'Morgan', 'Arthur', 'yoHan', 'Chovy', 'Deft', 'Vsta', 'Hoya', 'Chieftain', 'UmTi', 'Lava', 'Hena', 'Delight', 'Chasy', 'Khan', 'Canyon', 'ShowMaker', 'Ghost', 'BeryL', 'Destroy', 'Kingen', 'Pyosik', 'SOLKA', 'BAO', 'Becca']
    year = '2020'
    player_stats(year, players, 'lck') 
    players_no_stats_by_year('2020')

def main(): 
    year = '2021'
    read_roster_csv(year) 
    players_no_stats_by_year(year)

if __name__ == "__main__":
    main()
    # test()