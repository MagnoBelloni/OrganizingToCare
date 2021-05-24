from app import app, db
from app.models.medicamento import Medicamento
from flask import Flask, render_template, request, redirect, url_for
from flask import  flash, get_flashed_messages, json, jsonify


@app.route("/medicamento")
def index_medicamentos():
    medicamentos = Medicamento.query.all()
    return render_template("medicamento/index.html", medicamentos=medicamentos)


@app.route("/medicamento/novo")
def novo_medicamento():
    if request.method =='POST':
        # crio um objeto cliente com os dados do formulário 
        medicamento = Medicamento(
        request.form['nome_medicamento'],
        request.form['data_validade'],
        request.form['quantidade'],
        request.form['peso'])
        db.session.add(medicamento)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("medicamento/novo.html")

    if request.form['nome_medicamento'] == '':
        flash('Nome do medicamento é obrigatório!')

    if request.form['data_validade'] == '':
        flash('A data de validade é obrigatória!')

    if request.form['quantidade'] == '':
        flash('A quantidade é obrigatória!')

    if len(get_flashed_messages()) > 0:
        return render_template("medicamento/novo.html")



@app.route("/medicamento/editar/<int:id>")
def editar_medicamento():
    # select from 
    medicamento = Medicamento.query.get(id)
    if request.method == 'POST':
        medicamento.nome_medicamento = request.form['nome_medicamento']
        medicamento.data_validade = request.form['data_validade']
        medicamento.quantidade = request.form['quantidade']
        medicamento.peso = request.form['peso']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("medicamento/editar.html", medicamento = medicamento)     


@app.route("/medicamento/excluir/<int:id>")
def excluir_medicamento(id):
    medicamento = Medicamento.query.get(id)
    db.session.delete(medicamento)
    db.session.commit()
    return redirect(url_for("index"))
