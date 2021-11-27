from app import app, db
from app.models.pacientes import Paciente
from app.models.medicamento import Medicamento
from app.helpers.calcula_idade import CalcularIdade
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, get_flashed_messages, json, jsonify
from datetime import datetime

@app.route("/paciente")
def index_pacientes():
    pacientes = Paciente.query.all()
    return render_template("paciente/index.html", pacientes=pacientes)

@app.route("/paciente/novo", methods=['POST', 'GET'])
def novo_paciente():
    if request.method == 'POST':
        dataNascimentoFormatada = datetime.strptime(
            request.form['dataNascimento'], '%Y-%m-%d')
            
        dataInternacaoFormatada = datetime.strptime(
            request.form['dataInternacao'], '%Y-%m-%d')

        paciente = Paciente(
            request.form['nome'],
            dataNascimentoFormatada,
            request.form['altura'],
            request.form['peso'],
            request.form['nomeResponsavel'],
            request.form['telefoneResponsavel'],
            dataInternacaoFormatada)

        db.session.add(paciente)
        db.session.commit()
        return redirect(url_for('index_pacientes'))
    return render_template('paciente/novo.html')



@app.route("/paciente/editar/<int:id>", methods=['GET', 'POST'])
def editar_paciente(id):  
    paciente = Paciente.query.get(id)
    if request.method == 'POST':
        dataNascimentoFormatada = datetime.strptime(
            request.form['dataNascimento'], '%Y-%m-%d')
            
        dataInternacaoFormatada = datetime.strptime(
            request.form['dataInternacao'], '%Y-%m-%d')

        paciente.nome = request.form['nome']
        paciente.dataNascimento = dataNascimentoFormatada
        paciente.altura = request.form['altura']
        paciente.peso = request.form['peso']
        paciente.nomeResponsavel = request.form['nomeResponsavel']
        paciente.telefoneResponsavel = request.form['telefoneResponsavel']
        paciente.dataInternacao = dataInternacaoFormatada

        db.session.commit()
        return redirect(url_for('index_pacientes'))
    paciente.idade = CalcularIdade(paciente.dataNascimento)
    return render_template("paciente/editar.html", paciente=paciente)


@app.route("/paciente/excluir/<int:id>")
def excluir_paciente(id):
    medicamento = Paciente.query.get(id)
    db.session.delete(medicamento)
    db.session.commit()
    return redirect(url_for("index_pacientes"))

@app.route("/paciente/buscar", methods=["GET"])
def buscar_paciente():
    nome = request.form['nome']
    paciente = Paciente.query.filter((Paciente.nome == nome)).first()
    return render_template("paciente/index.html", paciente=paciente)