from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

import os
import json

import update_games

load_dotenv()

uri = os.getenv("MONGO_SERVER")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    db = client["ACBScrap"]
    col = db["games"]
    games = update_games.GamesUpdater()
    """
    data = games.scrap_url()
    for d in data:
        col.insert_one(d)
    """
    r = col.find({"id_week":2849})
    list(map(print, r))

    
    # print(col.find_one)
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
