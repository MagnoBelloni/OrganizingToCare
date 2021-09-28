from datetime import datetime
from app import db

class MedicamentoEstoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamentoPacienteId = db.Column(db.Integer, db.ForeignKey('medicamento_paciente.id'))
    dataVencimento = db.Column(db.DateTime, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    quantidadeInicial = db.Column(db.Integer, nullable=False)

    medicamento_estoque_registro_association = db.relationship('MedicamentoEstoqueRegistro', order_by='MedicamentoEstoqueRegistro.dataRegistro.desc()')

    def __init__(self, medicamentoPacienteId, dataVencimento, quantidade, quantidadeInicial):
        self.medicamentoPacienteId = medicamentoPacienteId
        self.dataVencimento = dataVencimento
        self.quantidade = quantidade
        self.quantidadeInicial = quantidadeInicial

    MedicamentoPaciente = db.relationship('MedicamentoPaciente', backref=db.backref("medicamento_estoque"))
