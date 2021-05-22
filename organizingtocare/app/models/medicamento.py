import datetime
from app import db


class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    dataVencimento = db.Column(db.DateTime)
    dataCriacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    quantidade = db.Column(db.String(10), nullable=False)
    peso = db.Column(db.String(50), nullable=False)
