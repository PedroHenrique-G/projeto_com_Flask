
# Documentação de Projetos Python com UV e Flask

## O que é o UV?

O **UV** é um gerenciador de pacotes e projetos para Python extremamente rápido, desenvolvido pela Astral e escrito em Rust. Ele substitui ferramentas como `pip`, `pip-tools`, `virtualenv`, `poetry` e `pyenv` em um único executável de altíssima performance.

---

## Instalação e Configuração Inicial

### 1. Instalação no Windows (PowerShell)

Obtemos a instrução de instalação oficial diretamente na documentação da Astral Docs:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

```

### 2. Comandos do Fluxo de Trabalho Executados

Após a instalação, executamos a sequência de comandos abaixo para estruturar o projeto:

```bash
# 1. Verificar a versão instalada do UV
uv -V

# 2. Criar um novo projeto Python do zero no diretório atual
uv init

# 3. Criar um ambiente virtual (.venv) isolado
uv venv

# 4. Sincronizar o ambiente virtual com o arquivo de trava (uv.lock)
uv sync

# 5. Adicionar e instalar a dependência do Flask no projeto
uv add flask

```

---

## 📁 Estrutura do Projeto e Desenvolvimento

Abaixo está a estrutura do projeto configurada no VS Code:

```text
projeto_com_Flask/
├── .venv/
├── templates/
│   └── ola.html
├── .gitignore
├── .python-version
├── app.py
├── pyproject.toml
├── README.md
└── uv.lock

```

### Código da Aplicação (`app.py`)



Criamos rotas com suporte a parâmetros na URL, sanitização de entrada com `escape` e renderização de templates Jinja2:

```python
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
def ola_nome(nome=None):
    return render_template('ola.html', nome=nome)

if __name__ == "__main__":
    app.run(debug=True, port=5000) # executar "flask run" no terminal

```

### Template HTML (`templates/ola.html`)



Arquivo HTML utilizando blocos condicionais do Jinja2 para renderizar saídas personalizadas:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olá do Flask</title>
</head>
<body>
    {% if nome %}
        <h1>Olá, {{nome}}!</h1>
    {% else %}
        <h1>Olá, Flask!</h1>
    {% endif %}
</body>
</html>

```

### Executando a Aplicação

Para rodar a aplicação Flask gerenciada pelo UV, utilizamos o comando no terminal:

```bash
uv run flask run

```

---

## Conceitos: Snippets

* **Snippet de Linha:** Instrução rápida gerada em uma única linha. É ideal para comandos simples ou chamadas de função diretas.
* **Snippet de Bloco:** Código estruturado contendo múltiplas linhas. Serve para criar estruturas complexas como funções, estruturas condicionais/loops ou páginas completas.

---

## Gerenciamento da Versão do Python com UV

O UV também permite gerenciar e instalar versões do próprio interpretador Python diretamente pelo terminal.

1. **Instalar uma versão específica do Python:**
```bash
uv python install 3.15.1

```


2. **Verificar a versão ativa:**
```bash
python -V

```