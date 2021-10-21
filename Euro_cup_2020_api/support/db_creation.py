from pymongo import MongoClient
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import csv 

#Load username and password from .env file
load_dotenv()
user = os.getenv("user")
password = os.getenv("pass")

#Connect to mongo Atlas server with admin username and password
url_connection = f"mongodb+srv://{user}:{password}@datacluster.2umgq.mongodb.net/test"
client = MongoClient(url_connection)

#Create the database and the collection
db = client['Euro_cup_2020']
db.segment.drop()
collection = db.segment

#open CSV file and read it
csvfile = open('/home/marrechea/Core/w1/d1/euro_2020/data/eurocup_2020.csv', 'r')
reader = csv.DictReader(csvfile)

#Create a list with the headers of the CSV file and then loop data, inserting them one by one into the db in JSON format.
header = ["stage", "date", "pens", "pens_home_score", "pens_away_score","team_name_home", "team_name_away", "team_home_score", "team_away_score", "possession_home", "possession_away", "total_shots_home", "total_shots_away", "shots_on_target_home", "shots_on_target_away", "duels_won_home", "duels_won_away", "events_list", "lineup_home", "lineup_away"]
for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
    db.segment.insert_one(row)


