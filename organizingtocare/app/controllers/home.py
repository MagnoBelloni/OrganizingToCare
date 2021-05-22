from app import app
from flask import render_template
from app.models.usuario import Usuario


@app.route("/home")
def home():
    return render_template("home.html")
