import requests
from dotenv import load_dotenv
import os

load_dotenv()
url_ = os.getenv("url")

def get_teams():
    url = f"{url_}/teams"
    teams = requests.get(url).json()
    return (teams)