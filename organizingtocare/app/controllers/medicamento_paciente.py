from app import app, db
from app.models.medicamento import Medicamento
from app.models.pacientes import Paciente
from app.models.medicamento_paciente import MedicamentoPaciente
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, get_flashed_messages
from datetime import datetime

paciente_id = 0

@app.route("/medicamento_paciente/novo/<int:paciente_id>", methods=['POST', 'GET'])
def novo_medicamento_paciente(paciente_id):
    paciente_id = paciente_id
    if request.method == 'POST':
        # if request.form['nome'] == '':
        #     flash('Nome do medicamento é obrigatório!')

        if len(get_flashed_messages()) > 0:
            return render_template("medicamento_paciente/novo.html")

        dataVencimentoFormatada = datetime.strptime(
                    request.form['dataVencimento'], '%Y-%m-%d')

        medicamento_paciente = MedicamentoPaciente(request.form['medicamentoId'], paciente_id, dataVencimentoFormatada, request.form['quantidade'])

        db.session.add(medicamento_paciente)

        db.session.commit()

        return redirect(f"/paciente/editar/{paciente_id}")
    medicamentos = MedicamentoPaciente.query.all()
    return render_template("medicamento_paciente/novo.html", medicamentos=medicamentos, paciente_id=paciente_id)


@app.route("/medicamento/editar/<int:id>", methods=['GET', 'POST'])
def editar_medicamento_paciente(id):   
    medicamento = Medicamento.query.get(id)

    if request.method == 'POST':
        medicamento.nome = request.form['nome']
        medicamento.descricao = request.form['descricao']
        db.session.commit()
        return redirect(url_for('index_medicamentos'))
    return render_template("medicamento/editar.html", medicamento=medicamento)


@app.route("/medicamento/excluir/<int:id>")
def excluir_medicamento_paciente(id):
    medicamento = Medicamento.query.get(id)
    db.session.delete(medicamento)
    db.session.commit()
    return redirect(url_for("index_medicamentos"))
