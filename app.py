from flask import Flask, render_template, request, g, redirect
from database.db import engine, get_decks


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")
@app.route("/study")
def study():
    if request.args.get("deck-id"):
        return render_template("study.html")
    else:
        return render_template("choose-deck.html", decks = get_decks())
    
@app.route("/add-decks")
def add_decks():
    return render_template("add-decks.html")    
@app.route("/add-cards")
def add_cards():
    return render_template("add-cards.html")    
@app.route("/browse")
def browse():
    return render_template("browse.html")        

if __name__ == "__main__":
    app.run(host="localhost", debug=True)