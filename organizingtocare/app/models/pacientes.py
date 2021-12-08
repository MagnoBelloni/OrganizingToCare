from datetime import datetime, date
from app import db

dataCriacao = datetime.now()
dataCriacaoString = dataCriacao.strftime('%d/%m/%Y %H:%M:%S')
dataCriacaoFormatada = datetime.strptime(dataCriacaoString,'%d/%m/%Y %H:%M:%S')

class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    dataNascimento = db.Column(db.DateTime, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    nomeResponsavel = db.Column(db.String(50), nullable=False)
    telefoneResponsavel = db.Column(db.String(50), nullable=False)
    dataInternacao = db.Column(db.DateTime, nullable=False)
    dataCriacao = db.Column(db.DateTime, default=dataCriacaoFormatada)

    medicamento_paciente_association = db.relationship('MedicamentoPaciente', viewonly=True)

    def __init__(self, nome, dataNascimento, altura, peso, nomeResponsavel, telefoneResponsavel, dataInternacao):
        self.nome = nome
        self.dataNascimento = dataNascimento.date()
        self.altura = altura
        self.peso = peso
        self.nomeResponsavel = nomeResponsavel
        self.telefoneResponsavel = telefoneResponsavel
        self.dataInternacao = dataInternacao
