from app import app
from flask import render_template
from app.models.medicamento import Medicamento
from datetime import datetime, timedelta


@app.route("/home")
def home():
    filtro_vencimento_em_dias = datetime.today() + timedelta(days=15)
    medicamentos_para_vencer = Medicamento.query.filter(
        Medicamento.dataVencimento <= filtro_vencimento_em_dias).all()
    for medicamento in medicamentos_para_vencer:
        medicamento.vencido = medicamento.dataVencimento < datetime.today()
    return render_template("home.html", medicamentos=medicamentos_para_vencer)
