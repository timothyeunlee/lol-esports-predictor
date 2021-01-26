import os 
import requests
from bs4 import BeautifulSoup
from pprint import pprint
 
def scrape_player_stats_2021(): 
    faker_url = 'https://lol.gamepedia.com/Faker/Statistics/2021' 
    
    page = requests.get(faker_url) 

    soup = BeautifulSoup(page.content, 'html.parser')

    stats_div = soup.find('div', {'class': 'wide-content-scroll'})
    # td = stats.find_all('td', {'class': 'spstats-subject'})
    stats = stats_div.find_all('td')

    stat_list = []
    for td in stats:
        stat_list.append(td.text)

    print(len(stat_list))
    print(stat_list)

# Games
# Win 
# Loss
# W/L Ratio
# Kill
# Death
# Assist
# KDA
# CS
# CS/M
# Gold
# Gold/M
# Kill Participation ((K+A) / Team K)
# Kill Share (K / Team K)
# Gold Share

# sample output 
# Azir
# 4
# 1
# 3
# 25%
# 2.5
# 2.75
# 4.25
# 2.45
# 272.5
# 8.18
# 12.3
# 370
# 65.9%
# 24.4%
# 21.7%
# Zoe
# 2
# 1
# 1
# 50%
# 1.5
# 1.5
# 5.5
# 4.67
# 276.5
# 7.75
# 12.3
# 345
# 58.3%
# 12.5%
# 19.6%

if __name__ == "__main__":
    scrape_player_stats_2021()