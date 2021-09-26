from datetime import datetime
from app import db

dataRegistro = datetime.now()
dataRegistroString = dataRegistro.strftime('%d/%m/%Y %H:%M:%S')
dataRegistroFormatada = datetime.strptime(dataRegistroString,'%d/%m/%Y %H:%M:%S')

class MedicamentoEstoqueRegistro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    medicamentoEstoqueId = db.Column(db.Integer, db.ForeignKey('medicamento_estoque.id'))
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    dataRegistro = db.Column(db.DateTime, default=dataRegistroFormatada)
    
    def __init__(self, medicamentoEstoqueId, usuarioId,  quantidade):
        self.medicamentoEstoqueId = medicamentoEstoqueId
        self.usuarioId = usuarioId
        self.quantidade = quantidade

    Medicamentoestoque = db.relationship('MedicamentoEstoque', backref=db.backref("medicamento_estoque_registro"))
    Usuario = db.relationship('Usuario', backref=db.backref("medicamento_estoque_registro"))