from datetime import datetime
from app import db

class MedicamentoPaciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamentoId = db.Column(db.Integer, db.ForeignKey('medicamento.id'))
    pacienteId = db.Column(db.Integer, db.ForeignKey('paciente.id'))
    quantidadeEsperada = db.Column(db.Integer, nullable=False)
    unidadeDeMedida = db.Column(db.String(40), nullable=False)

    medicamento_estoque_association = db.relationship('MedicamentoEstoque', viewonly=True, order_by="MedicamentoEstoque.dataVencimento.asc()")

    
    def __init__(self, medicamentoId, pacienteId, quantidadeEsperada, unidadeDeMedida):
        self.medicamentoId = medicamentoId
        self.pacienteId = pacienteId
        self.quantidadeEsperada = quantidadeEsperada
        self.unidadeDeMedida = unidadeDeMedida

    Medicamento = db.relationship('Medicamento', backref=db.backref("medicamento_paciente"))
    Paciente = db.relationship('Paciente', backref=db.backref("medicamento_paciente"))