from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from app.models.usuario import Usuario
from app.helpers.gera_senha import gerar_senha_aleatoria
from app.apis.via_cep import busca_cep


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(login=login, senha=senha).first()

        if not usuario:
            flash("Login incorreto!")
            return render_template("usuario/login.html")

        if usuario.ativo != True:
            flash("Seu usuário está inativo, procure a admnistração.")
            return render_template("usuario/login.html")

        session['usuario_id'] = usuario.id
        session['usuario_tipo'] = usuario.tipo

        if usuario.trocarSenha:
            return redirect("/usuario/alterar_senha")

        return redirect("/home")
    return render_template("usuario/login.html")


@app.route("/sair")
def sair():
    session['usuario_id'] = ""
    session['usuario_tipo'] = ""
    return redirect("/")


@app.route("/usuario")
def index_usuario():
    usuarios = Usuario.query.all()
    return render_template("usuario/index.html", usuarios=usuarios)


@app.route("/usuario/novo", methods=['GET', 'POST'])
def novo_usuario():
    if request.method == 'POST':
        senha = gerar_senha_aleatoria()
        cep = request.form['cep']
        logradouro = busca_cep(cep)
        usuario = Usuario(
            request.form['nome'], request.form['login'], request.form['tipo'], senha, cep, logradouro)

        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('.senha_gerada', mensagem="Usuario Criado", senha=senha))
    return render_template("usuario/novo.html")


@app.route("/usuario/editar/<int:id>", methods=['GET', 'POST'])
def editar_usuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.nomeCompleto = request.form['nome']
        usuario.login = request.form['login']
        usuario.tipo = request.form['tipo']
        ativo = bool(request.form.get('ativo'))
        usuario.cep = request.form['cep']
        usuario.logradouro = busca_cep(usuario.cep)
        usuario.ativo = ativo

        db.session.commit()

        session['usuario_tipo'] = usuario.tipo

        return redirect('/usuario')
    return render_template("usuario/editar.html", usuario=usuario)


@app.route("/usuario/excluir/<int:id>")
def excluir_usuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect("/usuario")


@app.route("/usuario/resetar_senha/<int:id>")
def resetar_senha(id):
    usuario = Usuario.query.get(id)
    senha = gerar_senha_aleatoria()
    usuario.senha = senha
    usuario.trocarSenha = True
    db.session.commit()
    return redirect(url_for('.senha_gerada', mensagem="Senha Resetada", senha=senha))


@app.route("/usuario/gerar_senha")
def senha_gerada():
    mensagem = request.args['mensagem']
    senha = request.args['senha']
    return render_template("usuario/senha_gerada.html", mensagem=mensagem, senha=senha)


@app.route("/usuario/alterar_senha", methods=['GET', 'POST'])
def alterar_senha():
    if request.method == 'POST':
        usuario = Usuario.query.get(session['usuario_id'])

        usuario.senha = request.form['senha']
        usuario.trocarSenha = False
        db.session.commit()

        return redirect('/home')
    return render_template("usuario/alterar_senha.html")
