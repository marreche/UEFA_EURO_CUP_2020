from src.app import app
from src.utils.get_data import get_teams, get_players
from src.utils.json_parser import serialize


@app.route("/teams")
@serialize
def teams():
    teams = get_teams()
    return (teams)


@app.route("/teams/players")
@serialize
def players():
    players = get_players()
    return (players)