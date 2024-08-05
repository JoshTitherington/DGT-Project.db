from flask import Flask, redirect, url_for, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/games")
def games():
    return render_template("Page1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/videogame")
def videogame():
    return render_template("videogame.html")

if __name__ == "__main__":
    app.run()