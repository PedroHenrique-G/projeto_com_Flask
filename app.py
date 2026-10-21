from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def ola_mundo():
    return '<p>Olá, mundo!<p>'

@app.route("/pessoa")
def ola_pessoa():
    nome = request.args.get("nome", "Flask")
    return f'Olá, {escape(nome)}'

@app.route("/usuario/<username>")
def home_usuario(username):
    return f'<p>Usuário: {escape(username)}</p>'

@app.route("/ola/")
@app.route("/ola/<nome>")
def ola_nome(nome = None):
    return render_template('ola.html', nome=nome)

if __name__=="__main__":
    app.run(debug=True, port=5000) # executar "flask run" no terminal