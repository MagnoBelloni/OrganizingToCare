import os
import json
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

with open('./credentials/AppConfig.json') as jsonFile:
    dataFromJson = json.load(jsonFile)
    
host = dataFromJson["host"]
port = dataFromJson["port"]
user = dataFromJson["user"]
password = dataFromJson["password"]
database = dataFromJson["database"]

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CHAVE_SECRETA'
db = SQLAlchemy(app)

from app.controllers.default import *