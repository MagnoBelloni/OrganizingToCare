from app import app
from flask import render_template
from app.models.usuario import Usuario


@app.route("/")
def login():
    return render_template("usuario/login.html")


@app.route("/cadastro")
def cadastro():
    return render_template("usuario/cadastro.html")
