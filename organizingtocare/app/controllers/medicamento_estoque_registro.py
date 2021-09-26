from app import app, db
from app.models.medicamento_estoque_registro import MedicamentoEstoqueRegistro
from app.models.medicamento_estoque import MedicamentoEstoque
from flask import Flask, render_template, request, redirect, url_for, session
from flask import flash, get_flashed_messages
from datetime import datetime


@app.route("/medicamento_estoque_registro/novo/<int:medicamento_estoque_id>", methods=['POST', 'GET'])
def novo_medicamento_estoque_registro(medicamento_estoque_id):
    if request.method == 'POST':
        medicamento_estoque = MedicamentoEstoque.query.get(medicamento_estoque_id)
        quantidadeRetirada = int(request.form['quantidade'])
        if medicamento_estoque.quantidade < quantidadeRetirada:
            flash('Quantidade retirada é maior que a quantidade restante!')
            return render_template("medicamento_estoque/editar.html", medicamento_estoque=medicamento_estoque)

        medicamento_estoque.quantidade -= quantidadeRetirada
        medicamento_estoque_registro = MedicamentoEstoqueRegistro(
            medicamento_estoque_id,
            session['usuario_id'],
            quantidadeRetirada)
        
        db.session.add(medicamento_estoque_registro)
        db.session.commit()
        return redirect(f"/medicamento_estoque/editar/{medicamento_estoque_id}")


@app.route("/medicamento_estoque_registro/editar/<int:id>", methods=['GET', 'POST'])
def editar_medicamento_estoque_registro(id):
    if request.method == 'POST':
        medicamento_estoque_registro = MedicamentoEstoqueRegistro.query.get(id)
        medicamento_estoque = MedicamentoEstoque.query.get(medicamento_estoque_registro.medicamentoEstoqueId)
        
        medicamento_estoque_id = medicamento_estoque.id

        quantidade = int(request.form['quantidade'])
        if medicamento_estoque.quantidade < quantidade:
            flash('Quantidade retirada é maior que a quantidade restante!')
            return render_template("medicamento_estoque/editar.html", medicamento_estoque=medicamento_estoque)

        if quantidade < medicamento_estoque_registro.quantidade:
            medicamento_estoque.quantidade += medicamento_estoque_registro.quantidade

        medicamento_estoque.quantidade -= quantidade
        medicamento_estoque_registro.quantidade = quantidade

        db.session.commit()
        return redirect(f"/medicamento_estoque/editar/{medicamento_estoque_id}")


@app.route("/medicamento_estoque_registro/excluir/<int:id>")
def excluir_medicamento_estoque_registro(id):
    medicamento_estoque_registro = MedicamentoEstoqueRegistro.query.get(id)
    medicamento_estoque = MedicamentoEstoque.query.get(medicamento_estoque_registro.medicamentoEstoqueId)

    medicamento_estoque.quantidade += medicamento_estoque_registro.quantidade
    medicamento_estoque_id = medicamento_estoque.id
    
    db.session.delete(medicamento_estoque_registro)
    db.session.commit()

    return redirect(f"/medicamento_estoque/editar/{medicamento_estoque_id}")
