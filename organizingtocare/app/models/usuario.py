import datetime
from app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeCompleto = db.Column(db.String(80), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    trocarSenha = db.Column(db.Boolean, default=True)
    dataCriacao = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, nome, login, tipo, senha):
        self.nomeCompleto = nome
        self.login = login
        self.tipo = tipo
        self.senha = senha
