from flask import Flask, render_template, request, g, redirect
from database.db import engine, get_decks


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html", decks = get_decks())    

if __name__ == "__main__":
    app.run(host="localhost", debug=True)