from src.app import app
from src.utils.get_data import get_euro_stages,euro_data_stage, euro_data_players
from src.utils.json_parser import serialize
from flask import render_template


@app.route("/")
def home():
    return (render_template('home.html'))

@app.route("/menu")
def menu():
    return {
        "/all" : "Shows all available data in this api",
        "/stages" : "Returns EURO CUP 2020 stages",
        "/stages/final" : "EURO CUP 2020 Final",
        "/stages/semis" : "EURO CUP 2020 Semi-Finals",
        "/stages/quarter" : "EURO CUP 2020 Quarter-Finals",
        "/stages/sixteen" : "EURO CUP 2020 Round of Sixteen",
        "/stages/groups1" : "EURO CUP 2020 Groups Day One",
        "/stages/groups2" : "EURO CUP 2020 Groups Day Two",
        "/stages/groups3" : "EURO CUP 2020 Groups Day Three",
        "/teams" : "EURO CUP 2020 Participating Countries"
    }

@app.route("/all")
@serialize
def all():
    return {"all_data": (euro_data_stage, euro_data_players)}

@app.route("/stages")
@serialize
def stages():
    euro_stages = get_euro_stages()
    return (euro_stages)

