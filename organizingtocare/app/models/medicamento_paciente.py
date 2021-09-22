from datetime import datetime
from app import db

class MedicamentoPaciente(db.Model):
    medicamentoId = db.Column(db.Integer, db.ForeignKey('medicamento.id'), primary_key=True)
    pacienteId = db.Column(db.Integer, db.ForeignKey('paciente.id'), primary_key=True)
    dataVencimento = db.Column(db.DateTime, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    unidadeDeMedida = db.Column(db.String(40), nullable=False)
    
    def __init__(self, medicamentoId, pacienteId, dataVencimento, quantidade, unidadeDeMedida):
        self.medicamentoId = medicamentoId
        self.pacienteId = pacienteId
        self.dataVencimento = dataVencimento
        self.quantidade = quantidade
        self.unidadeDeMedida = unidadeDeMedida

    Medicamento = db.relationship('Medicamento', backref=db.backref("medicamento_paciente"))
    Paciente = db.relationship('Paciente', backref=db.backref("medicamento_paciente"))