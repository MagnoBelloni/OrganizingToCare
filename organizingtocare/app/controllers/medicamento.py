from app import app
from app.models.medicamento import Medicamento
from flask import render_template


@app.route("/medicamento")
def index_medicamentos():
    medicamentos = Medicamento.query.all()
    return render_template("medicamento/index.html", medicamentos=medicamentos)


@app.route("/medicamento/novo")
def novo_medicamento():
    return render_template("medicamento/novo.html")


@app.route("/medicamento/editar/<int:id>")
def editar_medicamento():
    return render_template("medicamento/editar.html")


@app.route("/medicamento/excluir/<int:id>")
def excluir_medicamento():
    return redirect("/medicamento")
