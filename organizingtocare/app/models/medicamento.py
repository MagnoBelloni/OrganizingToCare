from app import db


class Medicamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    data_vencimento = db.Column(db.DateTime, nullable=False)
    quantidade = db.Column(db.String(40), nullable=False)
