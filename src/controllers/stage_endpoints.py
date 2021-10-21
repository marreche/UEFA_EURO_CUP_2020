from src.app import app
from src.utils.get_data import get_final, get_groups_day_one, get_groups_day_two,get_groups_day_three,get_semifinal,get_quarterfinal,get_round_of_sixteen
from src.utils.json_parser import serialize

@app.route("/stages/final")
@serialize
def final():
    euro_final = get_final()
    return (euro_final)

@app.route("/stages/semis")
@serialize
def semi_final():
    euro_semi_final = get_semifinal()
    return (euro_semi_final)

@app.route("/stages/quarter")
@serialize
def quarter_final():
    euro_quarter_final = get_quarterfinal()
    return (euro_quarter_final)

@app.route("/stages/sixteen")
@serialize
def round_of_sixteen():
    euro_round_of_sixteen = get_round_of_sixteen()
    return (euro_round_of_sixteen)

@app.route("/stages/groups1")
@serialize
def groups_day_one():
    euro_groups_day_one = get_groups_day_one()
    return (euro_groups_day_one)

@app.route("/stages/groups2")
@serialize
def groups_day_two():
    euro_groups_day_two = get_groups_day_two()
    return (euro_groups_day_two)

@app.route("/stages/groups3")
@serialize
def groups_day_three():
    euro_groups_day_three = get_groups_day_three()
    return (euro_groups_day_three)