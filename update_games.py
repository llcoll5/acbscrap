from dotenv import load_dotenv

import os
import json

import scraper_funcs

load_dotenv()

class Games(scraper_funcs.Scraper):
    def __init__(self):
        super().__init__()
        self.url_base = self.urls_base["games_list"]
        self.url_to_scrap = self.url_base

    def scrap_url(self):
        data = super().scrap_url()
        if isinstance(data, list):
            return data
        else:
            print("Failed to retrieve data or data is not in expected format.")
            return []

class GamesUpdater(scraper_funcs.Scraper):
    def __init__(self):
        super().__init__()
        self.url_base = self.urls_base["games"]
        self.url_to_scrap = self.url_base

    def update_season(self, season:int=None):
        if season == None:
            return None



if __name__ == "__main__":
    games = Games()
    data = games.scrap_url()
    print(type(data[0]))
    print(f"Retrieved {len(data)} items.")
    print(f"First item: {data[0]}")
    print(f"Ids of each game: {sorted([game['id'] for game in data])}")
    for game in data:
        if game["year"] == 2025:
            print(f"Game ID: {game['id']}, Current Matchweek ID: {game['id_current_matchweek']}")
    """
    with open(r'./pbp.json', 'w') as doc:
        for item in data:
            doc.write("%s\n" % item)
    """
