from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("user")
password = os.getenv("pass")

url = f"mongodb+srv://{username}:{password}@datacluster.2umgq.mongodb.net/Euro_cup_2020?retryWrites=true&w=majority"
client = MongoClient(url)

db = client.get_database("Euro_cup_2020")
stats = db.segment
players = db.players