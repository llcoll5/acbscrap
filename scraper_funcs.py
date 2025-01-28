from dotenv import load_dotenv

import requests
import os

load_dotenv()

class Scraper():
    def __init__(self):
        self.urls_base = {
            "games" : os.getenv("URL_GAMES"),
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

