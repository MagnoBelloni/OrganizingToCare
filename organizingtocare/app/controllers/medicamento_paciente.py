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
        dataVencimentoFormatada = datetime.strptime(
                    request.form['dataVencimento'], '%Y-%m-%d')

        medicamento_paciente = MedicamentoPaciente(
            request.form['medicamentoId'],
            paciente_id,
            dataVencimentoFormatada,
            request.form['quantidade'],
            request.form['unidadeDeMedida'])

        db.session.add(medicamento_paciente)
        db.session.commit()

        return redirect(f"/paciente/editar/{paciente_id}")
    medicamentos = Medicamento.query.all()
    return render_template("medicamento_paciente/novo.html", medicamentos=medicamentos, paciente_id=paciente_id)


@app.route("/medicamento_paciente/editar/<int:medicamentoId>/<int:pacienteId>", methods=['GET', 'POST'])
def editar_medicamento_paciente(medicamentoId, pacienteId):   
    medicamentos = Medicamento.query.all()
    medicamento_paciente = MedicamentoPaciente.query.filter_by(medicamentoId=medicamentoId, pacienteId=pacienteId).first()

    if request.method == 'POST':
        medicamento_paciente_existe = MedicamentoPaciente.query.filter_by(medicamentoId=request.form['medicamentoId'], pacienteId=pacienteId).first()
        if medicamento_paciente_existe:
            flash('Já existe um medicamento desse tipo vinculado a esse paciente!!')
            return render_template("medicamento_paciente/editar.html", medicamentos=medicamentos, medicamento_paciente=medicamento_paciente)

        dataVencimentoFormatada = datetime.strptime(
                    request.form['dataVencimento'], '%Y-%m-%d')

        medicamento_paciente.dataVencimento = dataVencimentoFormatada
        medicamento_paciente.quantidade = request.form['quantidade']
        medicamento_paciente.medicamentoId = request.form['medicamentoId']
        medicamento_paciente.unidadeDeMedida = request.form['unidadeDeMedida']

        db.session.commit()
        return redirect(f"/paciente/editar/{pacienteId}")
    return render_template("medicamento_paciente/editar.html", medicamentos=medicamentos, medicamento_paciente=medicamento_paciente)


@app.route("/medicamento_paciente/excluir/<int:medicamentoId>/<int:pacienteId>")
def excluir_medicamento_paciente(medicamentoId, pacienteId):
    medicamento_paciente = MedicamentoPaciente.query.filter_by(medicamentoId=medicamentoId, pacienteId=pacienteId).first()
    db.session.delete(medicamento_paciente)
    db.session.commit()
    return redirect(f"/paciente/editar/{pacienteId}")
