import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

file_path = os.path.abspath(os.getcwd())+"\organizingtocare.db"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{file_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'CHAVE_SECRETA'
db = SQLAlchemy(app)

from app.controllers.default import *
