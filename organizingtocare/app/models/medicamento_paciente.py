from datetime import datetime
from app import db

class MedicamentoPaciente(db.Model):
    medicamentoId = db.Column(db.Integer, db.ForeignKey('medicamento.id'), primary_key=True)
    pacienteId = db.Column(db.Integer, db.ForeignKey('paciente.id'), primary_key=True)
    dataVencimento = db.Column(db.DateTime, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)

    def __init__(self, medicamentoId, pacienteId, dataVencimento, quantidade):
        self.medicamentoId = medicamentoId
        self.pacienteId = pacienteId
        self.dataVencimento = dataVencimento
        self.quantidade = quantidade

    Medicamento = db.relationship('Medicamento', backref=db.backref("medicamento_paciente"))
    Paciente = db.relationship('Paciente', backref=db.backref("medicamento_paciente"))