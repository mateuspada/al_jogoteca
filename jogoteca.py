from flask import Flask, render_template, request, redirect, session, flash, url_for

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista_jogos = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome=nome
        self.nickname=nickname
        self.senha=senha

usuario1 = Usuario('Teste da Silva', 'teste', 'teste')
usuario2 = Usuario('Teste Dois', 'teste2', 'teste2')
usuario3 = Usuario('Teste Tres', 'teste3', 'teste3')
usuarios = {usuario1.nickname: usuario1,
            usuario2.nickname: usuario2,
            usuario3.nickname: usuario3}

app = Flask(__name__)
app.secret_key = 'flask_study'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima') or '/'
    return render_template('login.html', titulo='Faça seu login', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    proxima_pagina = request.form['proxima']

    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(f'{usuario.nickname} logado com sucesso!')
            return redirect(proxima_pagina)

    flash('Usuario ou senha inválido!')
    return redirect(url_for('login', proxima=proxima_pagina))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

app.run(port=8080, debug=True)
