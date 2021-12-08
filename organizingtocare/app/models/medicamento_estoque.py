from datetime import datetime
from app import db

class MedicamentoEstoque(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamentoPacienteId = db.Column(db.Integer, db.ForeignKey('medicamento_paciente.id'))
    dataVencimento = db.Column(db.DateTime, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    quantidadeInicial = db.Column(db.Integer, nullable=False)
    lote = db.Column(db.String, nullable=False)
    nomePessoaTrouxeMedicamento = db.Column(db.String, nullable=False)

    medicamento_estoque_registro_association = db.relationship('MedicamentoEstoqueRegistro', viewonly=True,order_by='MedicamentoEstoqueRegistro.dataRegistro.desc()')

    def __init__(self, medicamentoPacienteId, dataVencimento, quantidade, quantidadeInicial, lote, nomePessoaTrouxeMedicamento):
        self.medicamentoPacienteId = medicamentoPacienteId
        self.dataVencimento = dataVencimento
        self.quantidade = quantidade
        self.quantidadeInicial = quantidadeInicial
        self.lote = lote
        self.nomePessoaTrouxeMedicamento = nomePessoaTrouxeMedicamento

    MedicamentoPaciente = db.relationship('MedicamentoPaciente', backref=db.backref("medicamento_estoque"))
