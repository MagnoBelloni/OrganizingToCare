from app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(30), nullable=False)
    tipo = db.Column(db.String(40), nullable=False)
