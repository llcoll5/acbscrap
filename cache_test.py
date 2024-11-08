import requests
import time

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

# URL y headers de la solicitud
url = "https://api2.acb.com/api/v1/openapilive/Weeks/current?idCompetition=1&idEdition=89"
games = "https://api2.acb.com/api/v1/openapilive/Matches/matchesbyweeklite"
boxscore = "https://api2.acb.com/api/v1/openapilive/Boxscore/playermatchstatistics?idMatch="
pbp = "https://api2.acb.com/api/v1/openapilive/PlayByPlay/matchevents?idMatch="

headers = {
    "Authorization": "H4sIAAAAAAAAA32Ry3aqMBSG36iLi7qOw4oFk9PEQyohZEYilkCirIMF5OkbOmiVQUdZ+/bv798pbrAUkVR7BUEyAhcr0IIzWcoArEDdMBrA9VNxg5BPiQqp1wDGnEGTp/009MIZD4sd0dIsSxFMw7ATUaL2ulWxN7jZGV2poTegehuvrzKiTp7iRniL7zxhoZuzTZl5uhPKTTkD055Q+qTkkR6Pka4y9qNDTDjyu/hg6zxdVnkajq+UazmZ0Bstz7gT5j5HGhmtx4MPa9s/34dyxvUj41LL22OdMOxkqdXxSZN5d9r10BwNDS2v5Vh/zPg8ntD6W9OhwzHVvfDnPU033ZFHL495uinlmTTcsv/q5Yshmc+2GdNB8fXWs32wK3a4Ej7UMx8JT13LBy3LvUdsNXDDjf2P2X3YW6+EgQZUlwEf6gXeIgdvk4W9my52z2pfAReNcY8q1KPte4+CXtn/cub9p/jJef7j/Xvf/j150Sag6C1ctS41qVe3p6Fml5U4gf/xdecli8sn/TA0Eb8CAAA="
}

type_url = "pbp"
pbp = pbp + "103836"
cache = DataCache(pbp, headers)

data = cache.fetch_data()

if type(data) == list and type_url == "games": 
    year_games = []
    for game in data:
        year = game["edition"]["year"]
        if year == 2023:
            year_games.append(game)
            print(game)
    print(f"Hi ha {len(year_games)} elements a dins de data")
elif type_url == "boxscore":
    print(data)
else:
    print(data)

