from cassiopeia import riotapi
import os

riotapi.set_region("EUW")
KEY = os.environ["DEV_KEY"]
riotapi.set_api_key(KEY)

summonerName = input("Please enter summoner name: ")
isNameInvalid = True

while isNameInvalid:
    try:
        summoner = riotapi.get_summoner_by_name(summonerName)
    except:
        summonerName = input("No summoner by that name found, please enter a valid summoner name: ")
    finally:
        summoner = riotapi.get_summoner_by_name(summonerName)
        isNameInvalid = False


matchHistory = summoner.match_list()

rkdMatchHistory = []
for match in matchHistory:
    if match.queue.name == "ranked_solo" or match.queue.name == "ranked_dynamic_queue":
        rkdMatchHistory.append(match)

metaRkdMatchHistory = []
for match in rkdMatchHistory:
    if (match.timestamp.now().toordinal() - match.timestamp.toordinal()) <= 31:
        metaRkdMatchHistory.append(match)


#nPlayedRankedMonth = len(metaRkdMatchHistory)
#print("You've played {n} ranked games in the past month".format(n=nPlayedRankedMonth))