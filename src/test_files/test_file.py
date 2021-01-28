import os 
import requests
from bs4 import BeautifulSoup
from pprint import pprint


def gettingPlayerName(): 
    sample_dictionary = {
        'T1': {'Faker': 'Mid', 'Teddy': 'Bot', 'Canna': 'Jungler'}, 'DWG': {'Showmaker': 'Mid', 'Khan': 'Top'} 
    }

    for key in sample_dictionary.keys():
        for subkey in sample_dictionary[key].keys(): 
            print (subkey)
    

    # print(sample_dictionary)
# keys = []
# for k,p in sample_dictionary.items():
#     keys.append(p.keys())

# print(keys)


def testForReplacing(): 
    faker = ['Azir', '4', '1', '3', '25%', '2.5', '2.75', '4.25', '2.45', '272.5', '8.18', '12.3', '370', '65.9%', '24.4%', '21.7%', 
    'Zoe', '2', '1', '1', '50%', '1.5', '1.5', '5.5', '4.67', '276.5', '7.75', '12.3', '345', '58.3%', '12.5%', '19.6%']
    # print(len(faker))
    # print(faker)
    # for item in faker: 
        # print (item)
    count = 0
    new_dictionary = {} 
    for item in faker: 
        new_dictionary[count] = item
        # print(new_dictionary)
        count+=1
        if count == 16: 
            print(new_dictionary)
            new_dictionary.clear
            count = 0

def scrape_player_stats_by_year(player, player_dict, year):  
    player_url = 'https://lol.gamepedia.com/' + player + '/Statistics/' + year

    # faker_url = 'https://lol.gamepedia.com/Faker/Statistics/2021' 
    # print(player_url)    

    page = requests.get(player_url) 

    soup = BeautifulSoup(page.content, 'html.parser')
    # stats_div = soup.find('div', {'class': 'wide-content-scroll'})

    page_div = soup.find('div', {'class': 'mw-parser-output'})
    tournament_div = page_div.find_all('div', {'class': 'wide-content-scroll'})

    for tag in tournament_div: 
        tournament_name = tag.find('a', {'class': 'mw-redirect to_hasTooltip'})
        print(tournament_name.text)
        
        stats = tag.find_all('td')
        for stat in stats: 
            print (stat.text)

    # print(stats)

    # stat_list = []

    # count = 0
    # for td in stats:
        # stat_list.append(td.text)
        # count += 1
        # if count == 16: 
            # champion_dict = fill_player_champion_stats(stat_list)
            # print(stat_list)            
            # player_dict[player].update(champion_dict)
            # stat_list.clear()
            # count = 0
   
######################################################################################################################################################################################
# for team in sample_dictionary: 
#     for innerkey in team: 
#         print(innerkey)


# {'faker': {'Champion': 'Zoe', 'Games': '2', 'Win': '1', 'Loss': '1', 'W/L Ratio': '50%', 
# 'Kill': '1.5', 'Death': '1.5', 'Assist': '5.5', 'KDA': '4.67', 'CS': '276.5', 'CS/M': '7.75', 
# 'Gold': '12.3', 'Gold/M': '345', 'Kill Participation': '58.3%', 'Kill Share': '12.5%', 'Gold Share': '19.6%'}}

if __name__ == "__main__":
    # gettingPlayerName()
    sample_dict = {}
    sample_dict['Faker'] = {}
    scrape_player_stats_by_year('Faker', sample_dict, '2020')
    # testForReplacing()


    