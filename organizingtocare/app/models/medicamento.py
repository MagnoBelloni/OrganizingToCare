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
    # dataVencimento = db.Column(db.DateTime, nullable=False)
    # quantidade = db.Column(db.String(10), nullable=False)
    # peso = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

    # def __init__(self, nome, dataVencimento, quantidade, peso):
    #     self.nome = nome
    #     self.dataVencimento = dataVencimento.date()
    #     self.quantidade = quantidade
    #     self.peso = peso
