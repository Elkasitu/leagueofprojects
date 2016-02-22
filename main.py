from cassiopeia import riotapi
from cassiopeia.type.core.common import Queue

import os

#TODO: Set a proper way to select server
riotapi.set_region("EUW")

# We get the key as an environment variable called DEV_KEY so that it's not exposed in the code
KEY = os.environ["DEV_KEY"]
riotapi.set_api_key(KEY)

# We only get ranked games (S6 onwards)
Q = Queue.ranked_dynamic_queue

# We ask the user for a summoner name, this is just for testing purposes, this is supposed to be backend
# only
summonerName = input("Please enter summoner name: ")

# We check if the summoner name is invalid and keep asking if it's not
isNameInvalid = True
while isNameInvalid:
    try:
        summoner = riotapi.get_summoner_by_name(summonerName)
    except:
        summonerName = input("No summoner by that name found, please enter a valid summoner name: ")
    finally:
        summoner = riotapi.get_summoner_by_name(summonerName)
        isNameInvalid = False


# We get the summoner's match history, provided that it's a ranked game (Q) and up to a maximum of
# 50 matches (to be refined later on)
matchHistory = summoner.match_list(num_matches=50, ranked_queues=Q)
bans = {}

for match in matchHistory:
    fullMatch = match.match(include_timeline=False)
    blue = fullMatch.blue_team
    red = fullMatch.red_team

    for ban in blue.bans:
        if ban.champion.name not in bans.keys():
            bans[ban.champion.name] = 1
        else:
            bans[ban.champion.name] += 1

    for ban in red.bans:
        if ban.champion.name not in bans.keys():
            bans[ban.champion.name] = 1
        else:
            bans[ban.champion.name] += 1

print(bans)
