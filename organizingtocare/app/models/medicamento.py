from datetime import datetime
from app import db

dataCriacao = datetime.now()
dataCriacaoString = dataCriacao.strftime('%d/%m/%Y %H:%M:%S')
dataCriacaoFormatada = datetime.strptime(dataCriacaoString,'%d/%m/%Y %H:%M:%S')

class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    dataCriacao = db.Column(db.DateTime, default=dataCriacaoFormatada)
    psicotropico = db.Column(db.Boolean)

    def __init__(self, nome, descricao, psicotropico):
        self.nome = nome
        self.descricao = descricao
        self.psicotropico = psicotropico
