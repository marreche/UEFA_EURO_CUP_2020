from src.app import app
from src.utils.get_data import get_teams, get_players
from src.utils.json_parser import serialize
from src.utils.error_handling import errorHandling
from flask import request
from src.utils.error_handling import MissingArgumentError
from src.utils.atlas_connection import players


@app.route("/teams")
@errorHandling
@serialize
def teams():
    teams = get_teams()
    return (teams)


@app.route("/teams/players")
@errorHandling
@serialize
def players():
    players = get_players()
    return (players)

@app.route("/players/search")
@errorHandling
@serialize
def player_search():
    pattern = request.args.get("name")
    if not pattern:
        raise MissingArgumentError("name")
    pattern = f".*{pattern.lower()}.*"
    res = players.find({"name":pattern})
    return (list(res))