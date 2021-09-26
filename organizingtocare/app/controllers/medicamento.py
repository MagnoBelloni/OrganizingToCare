from app import app, db
from app.models.medicamento import Medicamento
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, get_flashed_messages
from datetime import datetime


@app.route("/medicamento")
def index_medicamentos():
    medicamentos = Medicamento.query.order_by(Medicamento.psicotropico.desc()).all()
    return render_template("medicamento/index.html", medicamentos=medicamentos)

@app.route("/medicamento/novo", methods=['POST', 'GET'])
def novo_medicamento():
    if request.method == 'POST':
        if request.form['nome'] == '':
            flash('Nome do medicamento é obrigatório!')

        if len(get_flashed_messages()) > 0:
            return render_template("medicamento/novo.html")

        medicamento = Medicamento(
            request.form['nome'],
            request.form['descricao'],
            bool(request.form.get('psicotropico')))
        db.session.add(medicamento)
        db.session.commit()
        return redirect(url_for('index_medicamentos'))

    return render_template("medicamento/novo.html")


@app.route("/medicamento/editar/<int:id>", methods=['GET', 'POST'])
def editar_medicamento(id):   
    medicamento = Medicamento.query.get(id)

    if request.method == 'POST':
        medicamento.nome = request.form['nome']
        medicamento.descricao = request.form['descricao']
        medicamento.psicotropico = bool(request.form.get('psicotropico'))
        db.session.commit()
        return redirect(url_for('index_medicamentos'))
    return render_template("medicamento/editar.html", medicamento=medicamento)


@app.route("/medicamento/excluir/<int:id>")
def excluir_medicamento(id):
    medicamento = Medicamento.query.get(id)
    db.session.delete(medicamento)
    db.session.commit()
    return redirect(url_for("index_medicamentos"))
