import os 
import pandas 

def all_teams(): 
    all_teams = [
        # LCS
        '100 Thieves', 
        'Cloud9',
        'Counter Logic Gaming',
        'Dignitas', 
        'Evil Geniuses', 
        'FlyQuest',
        'Golden Guardians', 
        'Immortals',
        'Team Liquid',
        'TSM',
        # LEC 
        'Excel Esports',
        'FC Schalke 04 Esports',
        'Fnatic', 
        'G2 Esports', 
        'MAD Lions',
        'Misfits Gaming', 
        'Rogue',
        'Origen', # 2020
        'SK Gaming',
        'Team Vitality',
        'Astralis', 
        # LCK
        'T1', 
        'Gen.G', 
        'KT Rolster', 
        'Afreeca Freecs', 
        'Nongshim RedForce', 
        'Liiv SANDBOX', 
        'Hanwha Life Esports', 
        'Fredit BRION', 
        'DWG KIA', 
        'DRX',
        'DAMWON Gaming', # 2020
        'SANDBOX Gaming', #2020
        'Griffin', #2020
        'SeolHaeOne Prince', #2020
        # LPL 
        'Billibili Gaming',
        'Dominus Esports', # 2020
        'EDward Gaming', 
        'FunPlus Phoenix', 
        'Invictus Gaming',
        'JD Gaming',
        'LGD Gaming',
        'LNG Esports',
        'Oh My God',
        'Rogue Warriors',
        'Royal Never Give Up', 
        'Suning',
        'Team WE',
        'Top Esports',
        'Vici Gaming', # 2020 
        'Victory Five',
        'eStar',
        'Rare Atom', # 2021
        'ThunderTalk Gaming', # 2021
        # PCS 
        'ahq eSports Club',
        'Alpha Esports',
        'Berjaya Dragons',
        'Hong Kong Attitude',
        'J Team',
        'Liyab Esports',
        'Machi Esports',
        'Nova Esports',
        'Resurgence',
        'Talon Esports',
        'Impunity',
        'BOOM Esports',
        'Beyond Gaming',
        'PSG Talon'
    ]
    return all_teams

def df_export(df, out_dir, out_file):
    output_dir = out_dir
    output_file = out_file

    if not os.path.exists(output_dir):
        os.mkdir(output_dir) 
    
    complete_path = os.path.join(output_dir, output_file)
    df.to_csv(complete_path)