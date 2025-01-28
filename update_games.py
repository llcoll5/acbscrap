from dotenv import load_dotenv

import os
import json

import scraper_funcs

load_dotenv()

url = "https://api2.acb.com/api/v1/openapilive/Matches/matchesbyweeklite"

class GamesUpdater(scraper_funcs.Scraper):
    def __init__(self):
        super().__init__()
        self.url_base = self.urls_base["games"]
        self.url_to_scrap = self.url_base



if __name__ == "__main__":
    games = scraper_funcs.Scraper()
    data = games.scrap_url()
    print(type(data[0]))
    """
    with open(r'./pbp.json', 'w') as doc:
        for item in data:
            doc.write("%s\n" % item)
    """
