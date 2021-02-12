import os 
from os import listdir
from os.path import isfile, join 
import requests
import pandas as pd 
from bs4 import BeautifulSoup

def team_stats(team): 
    # lcs = ['100 Thieves', 'TSM', 'Team Liquid', 'Counter Logic Gaming', 'Golden Guardians', 'Evil Geniuses', 'Cloud9', 'Immortals', 'FlyQuest', 'Dignitas']
    # lec = ['SK Gaming', 'Astralis', 'Excel Esports', 'FC Schalke 04 Esports', 'Fnatic', 'G2 Esports', 'MAD Lions', 'Misfits Gaming', 'Rogue', 'Team Vitality'] 
    # lck = ['T1', 'Gen.G', 'KT Rolster', 'Afreeca Freecs', 'Nongshim RedForce', 'Liiv SANDBOX', 'Hanwha Life Esports', 'Fredit BRION', 'DWG KIA', 'DRX']

    scrape_team_stats_by_year(team)

def scrape_team_stats_by_year(team):
    team_url = 'https://lol.gamepedia.com/' + team + '/Match_History'

    page = requests.get(team_url) 

    soup = BeautifulSoup(page.content, 'html-parser') 
    
    try: 
        page_div = soup.find('div', {'class': 'mw-parser-output'})
        history_div = page_div.find('div', {'class' : 'wide-content-scroll'})

    except AttributeError: 
        print("attribute error")

def main(): 
    # scrape_team_stats_by_year()
    # team_stats()
    team_stats('T1')

def test():
    print ("test")

if __name__ == "__main__":
    main() 
