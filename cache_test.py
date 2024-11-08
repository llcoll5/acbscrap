import requests
import time
import random
from datetime import datetime
import json


class DataCache:
    def __init__(self, url, headers, cache_duration=300):
        self.url = url
        self.headers = headers
        self.cache_duration = cache_duration
        self.data = None
        self.last_fetched = None

    def fetch_data(self):
        if not self.data or (time.time()- self.last_fetched > self.cache_duration):
            response = requests.get(self.url, headers=self.headers)
            print("Not cached")
            if response.status_code == 200:
                self.data = response.json()
                self.last_fetched = time.time()
            else:
                print(f"Error: {response.status_code}")
                self.data = None
        return self.data
    
    def save_as_json(self, filename: str):
        data = self.fetch_data()
        with open(filename, "w") as file:
            json.dump(data, file)

# URL y headers de la solicitud
url = "https://api2.acb.com/api/v1/openapilive/Weeks/current?idCompetition=1&idEdition=89"
games = "https://api2.acb.com/api/v1/openapilive/Matches/matchesbyweeklite"
boxscore = "https://api2.acb.com/api/v1/openapilive/Boxscore/playermatchstatistics?idMatch="
pbp = "https://api2.acb.com/api/v1/openapilive/PlayByPlay/matchevents?idMatch="

headers = {
    "Authorization": "H4sIAAAAAAAAA32Ry3aqMBSG36iLi7qOw4oFk9PEQyohZEYilkCirIMF5OkbOmiVQUdZ+/bv798pbrAUkVR7BUEyAhcr0IIzWcoArEDdMBrA9VNxg5BPiQqp1wDGnEGTp/009MIZD4sd0dIsSxFMw7ATUaL2ulWxN7jZGV2poTegehuvrzKiTp7iRniL7zxhoZuzTZl5uhPKTTkD055Q+qTkkR6Pka4y9qNDTDjyu/hg6zxdVnkajq+UazmZ0Bstz7gT5j5HGhmtx4MPa9s/34dyxvUj41LL22OdMOxkqdXxSZN5d9r10BwNDS2v5Vh/zPg8ntD6W9OhwzHVvfDnPU033ZFHL495uinlmTTcsv/q5Yshmc+2GdNB8fXWs32wK3a4Ej7UMx8JT13LBy3LvUdsNXDDjf2P2X3YW6+EgQZUlwEf6gXeIgdvk4W9my52z2pfAReNcY8q1KPte4+CXtn/cub9p/jJef7j/Xvf/j150Sag6C1ctS41qVe3p6Fml5U4gf/xdecli8sn/TA0Eb8CAAA="
}

type_url = "games"
year = 2024
pbp = pbp + "103836"
boxscore = boxscore + "103836"
cache = DataCache(games, headers)
cache.save_as_json("games_list.json")
"""
data = cache.fetch_data()

if type(data) == list and type_url == "games": 
    year_games = [game for game in data if game["edition"]["year"] == year]
    print(f"Hi ha {len(year_games)} elements a dins de data")
    random_game = year_games[random.randint(0, len(year_games))]
    print(random_game)
    random_game_date = datetime.utcfromtimestamp(random_game["date"])
    print(f"El dia {random_game_date.strftime('%d-%m-%Y')} es juga el partit que enfronta {random_game['visitor_team']['team_actual_name']} al camp de {random_game['local_team']['team_actual_name']}, {random_game['arena']['name']}. Aquest serà un partit de la jornada {random_game['matchweek_number']}. El partit en principi es juga a les {random_game_date.strftime('%H:%M')}")
elif type_url == "boxscore":
    print(data[0].keys())
    print(data[10].keys())
else:
    print(data)



# Timestamp Unix integer provided
timestamp = 1748131200

# Convert timestamp to human-readable date
date = datetime.utcfromtimestamp(timestamp)
date.strftime("%Y-%m-%d %H:%M:%S")
print(date)

"""