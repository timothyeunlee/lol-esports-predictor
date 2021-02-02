import os
from dotenv import load_dotenv
from riotwatcher import LolWatcher, ApiError
import cassiopeia as cass
from cassiopeia import Summoner

load_dotenv()

cass.set_riot_api_key(os.getenv('RIOT_API_KEY'))

my_region = 'na1'
faker_region = 'KR'

summoner = 'Hide on bush'

def get_last_100games(): 
    Faker = Summoner(name = summoner, region= faker_region)
    
    # for match in Faker.match_history: 
    #     print (match)
    
    # me = Summoner(name="dlrmskla", region="NA")
    # print(me.champion_masteries)

    # SAMPLE PRINT OF Summoner.math_history 
    # Match(id=4950793053, region='KR')
    # Match(id=4950697908, region='KR')
    # Match(id=4950701334, region='KR')
    # Match(id=4950633649, region='KR')
    # Match(id=4950328244, region='KR')
    # Match(id=4950089568, region='KR')
    # Match(id=4949839491, region='KR')
    # Match(id=4949781996, region='KR')
    # Match(id=4949722862, region='KR')
    # Match(id=4949623872, region='KR')
    # Match(id=4949290954, region='KR')
    # Match(id=4949188862, region='KR')
    # Match(id=4949192017, region='KR')
    # Match(id=4949175136, region='KR')

if __name__ == "__main__":
    get_last_100games()


# 400 (Bad Request) This error indicates that there is a syntax error in the request and the request has therefore been denied. The client should not continue to make similar requests without modifying the syntax or the requests being made.

# Common Reasons

# A provided parameter is in the wrong format (e.g., a string instead of an integer).
# A provided parameter is invalid (e.g., beginTime and startTime specify a time range that is too large).
# A required parameter was not provided.
# 401 (Unauthorized) This error indicates that the request being made did not contain the necessary authentication credentials (e.g., an API key) and therefore the client was denied access. The client should not continue to make similar requests without including an API key in the request.

# Common Reasons

# An API key has not been included in the request.
# 403 (Forbidden) This error indicates that the server understood the request but refuses to authorize it. There is no distinction made between an invalid path or invalid authorization credentials (e.g., an API key). The client should not continue to make similar requests.

# Common Reasons

# An invalid API key was provided with the API request.
# A blacklisted API key was provided with the API request.
# The API request was for an incorrect or unsupported path.
# 404 (Not Found) This error indicates that the server has not found a match for the API request being made. No indication is given whether the condition is temporary or permanent.

# Common Reasons

# The ID or name provided does not match any existing resource (e.g., there is no Summoner matching the specified ID).
# There are no resources that match the parameters specified.
# 415 (Unsupported Media Type) This error indicates that the server is refusing to service the request because the body of the request is in a format that is not supported.

# Common Reasons

# The Content-Type header was not appropriately set.
# 429 (Rate Limit Exceeded) This error indicates that the application has exhausted its maximum number of allotted API calls allowed for a given duration. If the client receives a Rate Limit Exceeded response the client should process this response and halt future API calls for the duration, in seconds, indicated by the Retry-After header. Applications that are in violation of this policy may have their access disabled to preserve the integrity of the API. Please refer to our Rate Limiting documentation below for more information on determining if you have been rate limited, and how to avoid it.