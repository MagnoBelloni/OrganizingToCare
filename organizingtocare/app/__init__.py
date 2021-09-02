import os
import json
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

with open('./credentials/AppConfig.json') as jsonFile:
    data = json.load(jsonFile)

host = data["host"]
port = data["port"]
user = data["user"]
password = data["password"]

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CHAVE_SECRETA'
db = SQLAlchemy(app)

from app.controllers.default import *