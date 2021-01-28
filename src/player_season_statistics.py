import os 
import requests
from bs4 import BeautifulSoup
from pprint import pprint

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

def player_stats(year):
    # need to import csv and get player data keys 
    sample_player_dict = {
        # 'T1': {'Faker': 'Mid', 'Teddy': 'Bot', 'Canna': 'Jungler'}, 'DWG': {'Showmaker': 'Mid', 'Khan': 'Top'} 
        'T1': {'Faker': 'Mid'}, 'DWG': {'ShowMaker': 'Mid'}
        # 'T1': {'Faker': 'Mid'}
    }
    player_dict = {} 
    for team in sample_player_dict.keys():
        for player in sample_player_dict[team].keys():
            player_dict[player] = {} 
            scrape_player_stats_by_year(player, player_dict, year)

    print(player_dict)

def scrape_player_stats_by_year(player, player_dict, year):  
    player_url = 'https://lol.gamepedia.com/' + player + '/Statistics/' + year

    # faker_url = 'https://lol.gamepedia.com/Faker/Statistics/2021' 
    # print(player_url)    

    page = requests.get(player_url) 

    soup = BeautifulSoup(page.content, 'html.parser')

    stats_div = soup.find('div', {'class': 'wide-content-scroll'})
    # td = stats.find_all('td', {'class': 'spstats-subject'})
    stats = stats_div.find_all('td')

    stat_list = []

    count = 0
    for td in stats:
        stat_list.append(td.text)
        count += 1
        if count == 16: 
            champion_dict = fill_player_champion_stats(stat_list)
            
            # update (add layer of dictionary) to each player
            # every champion should be a new sub entry of the player 
            # { FAKER : { 'Azir' : ... , 'Zoe': .... } }
            player_dict[player].update(champion_dict)
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

def test():
    stat = {} 
    faker = ['Azir', '4', '1', '3', '25%', '2.5', '2.75', '4.25', '2.45', '272.5', '8.18', '12.3', '370', '65.9%', '24.4%', '21.7%', 'Zoe', '2', '1', '1', '50%', '1.5', '1.5', '5.5', '4.67', '276.5', '7.75', '12.3', '345', '58.3%', '12.5%', '19.6%']
    # print(make_dict_from_statlist(faker, stat))


if __name__ == "__main__":
    player_stats('2021')
    # scrape_player_stats_2021()
    # test()