import os
from dotenv import load_dotenv

load_dotenv()

# MY_ENV_VAR = os.getenv('MY_ENV_VAR')

riot_api_key = os.getenv('RIOT_API')

print (riot_api_key)