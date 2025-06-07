from dotenv import load_dotenv

import requests
import os

load_dotenv(override=True)

class Scraper():
    def __init__(self):
        self.urls_base = {
            "games" : os.getenv("URL_GAMES"),
            "games_list" : os.getenv("URL_GAMES_LIST"),
            "editions" : os.getenv("URL_EDITIONS"),
            "boxscore" : os.getenv("URL_BOXSCORE"),
            "pbp" : os.getenv("URL_PBP")
        }
        self.headers = {
            "Authorization" : os.getenv("HEADER_AUTHORIZATION")
        }
        self.url_to_scrap = self.urls_base.get("games")

    def scrap_url(self):
        response = requests.get(self.url_to_scrap, headers=self.headers)
        if response.status_code == 200:
            return response.json() 
        else:
            print(f"Error: {response.status_code}")
            return response.text

if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.scrap_url()
    if isinstance(data, list):
        print(f"Retrieved {len(data)} items.")
    else:
        print("Failed to retrieve data or data is not in expected format.")