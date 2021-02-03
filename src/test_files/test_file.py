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

def test_scrape(player, player_dict, year):  
    player_url = 'https://lol.gamepedia.com/' + player + '/Statistics/' + year
    # zeus_url = 'https://lol.gamepedia.com/Zeus/Statistics/2020'
    faker_url = 'https://lol.gamepedia.com/Faker/Statistics/2021' 
    # print(player_url)    

    page = requests.get(player_url) 

    soup = BeautifulSoup(page.content, 'html.parser')

    try: 
        page_div = soup.find('div', {'class': 'mw-parser-output'})
        tournament_div = page_div.find_all('div', {'class': 'wide-content-scroll'})
        for tag in tournament_div: 
            tournament_name = tag.find('a', {'class': 'mw-redirect to_hasTooltip'})
            # print(tournament_name.text)
        
            stats = tag.find_all('td')
            for stat in stats: 
                print (stat.text)
    except AttributeError:
        print ('att error')

def test_output_list(year): 
    # values = ['1', '2', '3']
    directory = '../'
    values = ['Fake', 'r', 'showmaker']
    file_name = 'no_player_stats' + year + '.txt'
    complete_path = os.path.join(directory, file_name)
    # if not os.path.exists(file_name): 
        # os.mkdir(file_name)
    file1 = open(complete_path, "w")
    print(file_name)
    file1.write(str(values))

if __name__ == "__main__":
    # gettingPlayerName()
    sample_dict = {}
    sample_dict['Faker'] = {}
    # sample_dict['Zeus'] = {}
    # test_output_list('2020')
    year = '2020'
    output_dir = './player_stats_csv/'
    year_dir = output_dir + '/' + year
    print(output_dir)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)
    # scrape_player_stats_by_year('Faker', sample_dict, '2020')
    # testForReplacing()
    # test_scrape('Faker', sample_dict, '2021') 
    # output_dir = './player_stats_csv/' + '2021'
    # print(output_dir)
