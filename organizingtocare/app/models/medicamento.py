import datetime
from app import db


class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    dataVencimento = db.Column(db.DateTime, nullable=False)
    dataCriacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    quantidade = db.Column(db.String(10), nullable=False)
    peso = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, dataVencimento, quantidade, peso):
        self.nome = nome
        self.dataVencimento = dataVencimento
        self.quantidade = quantidade
        self.peso = peso
