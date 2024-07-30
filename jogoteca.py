from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista_jogos = [jogo1, jogo2, jogo3]

app = Flask(__name__)
app.secret_key = 'flask_study'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)

    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo='Faça seu login')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if 'teste' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(f'{session['usuario_logado']} logado com sucesso!')
        return redirect('/')
    else:
        flash('Usuario não logado!')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect('/')

app.run(port=8080, debug=True)
