from app import app
from flask import render_template
from app.models.medicamento_estoque import MedicamentoEstoque
from datetime import datetime, timedelta


@app.route("/home")
def home():
    filtro_vencimento_em_dias = datetime.today() + timedelta(days=20)

    medicamentos_para_vencer = MedicamentoEstoque.query.filter(
        MedicamentoEstoque.dataVencimento <= filtro_vencimento_em_dias
    ).order_by(MedicamentoEstoque.dataVencimento.asc()).all()

    medicamentos_baixo_estoque = MedicamentoEstoque.query.filter(
        MedicamentoEstoque.quantidadeInicial / 3 >= MedicamentoEstoque.quantidade
    ).order_by(MedicamentoEstoque.quantidade.asc()).all()

    return render_template("home.html", medicamentos_para_vencer=medicamentos_para_vencer, medicamentos_baixo_estoque=medicamentos_baixo_estoque)
