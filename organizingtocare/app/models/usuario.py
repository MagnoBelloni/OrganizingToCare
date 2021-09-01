from datetime import datetime
from app import db

dataCriacao = datetime.now()
dataCriacaoString = dataCriacao.strftime('%d/%m/%Y %H:%M:%S')
dataCriacaoFormatada = datetime.strptime(dataCriacaoString,'%d/%m/%Y %H:%M:%S')

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomeCompleto = db.Column(db.String(80), nullable=False)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    trocarSenha = db.Column(db.Boolean, default=True)
    dataCriacao = db.Column(db.DateTime, default=dataCriacaoFormatada)
    cep = db.Column(db.String(8), nullable=False)
    logradouro = db.Column(db.String(40), nullable=False)

    def __init__(self, nome, login, tipo, senha, cep, logradouro):
        self.nomeCompleto = nome
        self.login = login
        self.tipo = tipo
        self.senha = senha
        self.cep = cep
        self.logradouro = logradouro
