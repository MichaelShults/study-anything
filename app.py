from flask import Flask, render_template, request, g, redirect
from database.db import get_decks, get_cards, decks, cards, engine, create_tables, add_deck, add_card, get_stats
from scripts.seed_db import seed


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", stats = get_stats())
@app.route("/study")
def study():
    if request.args.get("deck-id"):
        return render_template("study.html", cards = get_cards(int(request.args.get("deck-id"))))
    else:
        return render_template("choose-deck.html", decks = get_decks())
    
@app.route("/add-decks", methods=["GET", "POST"])
def add_decks():
    if request.method == "GET":
        return render_template("add-decks.html")
    else:
        add_deck(request.form["deck-name"])
        return redirect("/add-decks")

@app.route("/add-cards", methods=["POST", "GET"])
def add_cards():
    if request.method == "GET":
        return render_template("add-cards.html")
    else:
        add_card(int(request.form["deck-id"]), request.form["front"], request.form["back"])
        return redirect("/add-cards")
@app.route("/browse")
def browse():
    return render_template("browse.html", cards = get_cards())        

# create_tables()
# seed(decks, cards, engine)
