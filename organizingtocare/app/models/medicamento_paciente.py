from datetime import datetime
from app import db
# from app.models.medicamento import Medicamento

# medicamento_paciente_table = db.Table('medicamento_paciente',
#     db.Column('medicamento_id', db.Integer, db.ForeignKey('medicamento.id')),
#     db.Column('paciente_id', db.Integer, db.ForeignKey('paciente.id')),
#     db.Column('dataVencimento', db.DateTime),
#     db.Column('quantidade', db.String(10))
# )

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