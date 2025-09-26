from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

import os
import json

import update_games

import scraper_funcs

OVERRIDE = True
load_dotenv(override=OVERRIDE)


class Database():
    def __init__(self):
        self.uri = os.getenv("MONGO_SERVER")
        print(f"Connecting to MongoDB at {self.uri}")
        if not self.uri:
            raise ValueError("MONGO_SERVER environment variable is not set.")
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            self.db = self.client["ACBScrap"]
            self.games = self.db["games"]
            self.pbp = self.db["pbp"]
            self.boxscore = self.db["boxscore"]
        except Exception as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    db = Database()
    """
    data = games.scrap_url()
    for d in data:
        col.insert_one(d)
    """
    print(f"games: {db.games.count_documents({})}")
    # sc = scraper_funcs.Scraper()
    # data = sc.scrap_url()
    # db
    r = db.games.find({"id_week":2849})
    list(map(print, r))