from src.utils.atlas_connection import stats
from src.utils.atlas_connection import players

euro_data_stage = list(stats.find({}))
euro_data_teams = list(stats.find({}, {"_id": 0, "team_name_home": 1}))
euro_data_players = list(players.find({}))

def get_euro_stages():
    return {p["stage"]: p for p in euro_data_stage}

def get_final():
    return {"Final": euro_data_stage[0]}

def get_semifinal():
    return {
        "Semi-Final 1": euro_data_stage[1],
        "Semi-Final 2" : euro_data_stage[2]
        }
def get_quarterfinal():
    return {
        "Quarter-Finals 1": euro_data_stage[3],
        "Quarter-Finals 2" : euro_data_stage[4],
        "Quarter-Finals 3" : euro_data_stage[5],
        "Quarter-Finals 4" : euro_data_stage[6],
    }

def get_round_of_sixteen():
    return {
        "Round of Sixteen": euro_data_stage[7:15]
    }

def get_groups_day_three():
    return {
        "Group stage: Matchday 3" : euro_data_stage[15:27]
    }

def get_groups_day_two():
    return {
        "Group stage: Matchday 2" : euro_data_stage[27:39]
    }

def get_groups_day_one():
    return {
        "Group stage: Matchday 1" : euro_data_stage[39:51]
    }

def get_teams():
    team_name = []
    for team in euro_data_teams:
        teams = team["team_name_home"].strip()
        team_name.append(teams)
    unique_teams = (set(team_name))
    return {
        "Teams": unique_teams
    }

def get_players():
    return {
        "Players by Country": euro_data_players
    }
