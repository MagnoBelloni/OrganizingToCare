from app import app, db
from app.models.medicamento_estoque import MedicamentoEstoque
from flask import Flask, render_template, request, redirect, url_for
from flask import flash, get_flashed_messages
from datetime import datetime


@app.route("/medicamento_estoque/novo/<int:medicamento_paciente_id>", methods=['POST', 'GET'])
def novo_medicamento_estoque(medicamento_paciente_id):
    if request.method == 'POST':

        dataVencimentoFormatada = datetime.strptime(
            request.form['dataVencimento'], '%Y-%m-%d')

        medicamento_estoque = MedicamentoEstoque(
            medicamento_paciente_id,
            dataVencimentoFormatada,
            request.form['quantidade'],
            request.form['quantidade'],
            request.form['lote'],
            request.form['nomePessoaTrouxeMedicamento'])

        db.session.add(medicamento_estoque)
        db.session.commit()
        return redirect(f"/medicamento_paciente/editar/{medicamento_paciente_id}")

    return render_template(f"medicamento_estoque/novo.html", medicamento_paciente_id=medicamento_paciente_id)


@app.route("/medicamento_estoque/editar/<int:id>", methods=['GET', 'POST'])
def editar_medicamento_estoque(id):   
    medicamento_estoque = MedicamentoEstoque.query.get(id)

    if request.method == 'POST':
        medicamento_paciente_id = medicamento_estoque.MedicamentoPaciente.id

        dataVencimentoFormatada = datetime.strptime(
            request.form['dataVencimento'], '%Y-%m-%d')

        medicamento_estoque.quantidade = request.form['quantidade']
        medicamento_estoque.dataVencimento = dataVencimentoFormatada
        medicamento_estoque.lote = request.form['lote']
        medicamento_estoque.nomePessoaTrouxeMedicamento = request.form['nomePessoaTrouxeMedicamento']

        db.session.commit()
        return redirect(f"/medicamento_paciente/editar/{medicamento_paciente_id}")

    return render_template("medicamento_estoque/editar.html", medicamento_estoque=medicamento_estoque)


@app.route("/medicamento_estoque/excluir/<int:id>")
def excluir_medicamento_estoque(id):
    medicamento_estoque = MedicamentoEstoque.query.get(id)
    medicamento_paciente_id = medicamento_estoque.MedicamentoPaciente.id
    db.session.delete(medicamento_estoque)
    db.session.commit()
    return redirect(f"/medicamento_paciente/editar/{medicamento_paciente_id}")
