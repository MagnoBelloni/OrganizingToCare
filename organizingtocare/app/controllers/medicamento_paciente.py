from app import app, db
from app.models.medicamento import Medicamento
from app.models.pacientes import Paciente
from app.models.medicamento_paciente import MedicamentoPaciente
from app.models.medicamento_estoque import MedicamentoEstoque
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, get_flashed_messages
from datetime import datetime

paciente_id = 0
unidadesMedida = {
    "Litro": "l",
    "Mililitros": "ml",
    "Grama": "g",
    "Miligrama": "mg",
    "Micrograma": "mcg",
    "Kilograma": "kg",
    "Centímetro cúbico": "cc"
}

@app.route("/medicamento_paciente/novo/<int:paciente_id>", methods=['POST', 'GET'])
def novo_medicamento_paciente(paciente_id):
    paciente_id = paciente_id
    if request.method == 'POST':
        medicamento_paciente = MedicamentoPaciente(
            request.form['medicamentoId'],
            paciente_id,
            request.form['quantidade'],
            request.form['unidadeMedida'])

        db.session.add(medicamento_paciente)
        db.session.commit()

        return redirect(f"/paciente/editar/{paciente_id}")
    medicamentos = Medicamento.query.all()
    return render_template("medicamento_paciente/novo.html", medicamentos=medicamentos, paciente_id=paciente_id, unidadesMedida=unidadesMedida)


@app.route("/medicamento_paciente/editar/<int:id>", methods=['GET', 'POST'])
def editar_medicamento_paciente(id):
    medicamentos = Medicamento.query.all()
    medicamento_paciente = MedicamentoPaciente.query.get(id)

    if request.method == 'POST':
        medicamento_paciente.quantidade = request.form['quantidade']
        medicamento_paciente.medicamentoId = request.form['medicamentoId']
        medicamento_paciente.unidadeDeMedida = request.form['unidadeMedida']

        db.session.commit()
        return redirect(f"/paciente/editar/{medicamento_paciente.pacienteId}")

    # medicamento_paciente.quantidadeTotalRestante = sum(medicamento_paciente_dic.values()['quantidade'])
    return render_template("medicamento_paciente/editar.html", medicamentos=medicamentos, medicamento_paciente=medicamento_paciente, unidadesMedida=unidadesMedida)


@app.route("/medicamento_paciente/excluir/<int:id>")
def excluir_medicamento_paciente(id):
    medicamento_paciente = MedicamentoPaciente.query.get(id)
    db.session.delete(medicamento_paciente)
    db.session.commit()
    return redirect(f"/paciente/editar/{medicamento_paciente.pacienteId}")
