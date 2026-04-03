import os
from flask import Flask, render_template

# Criamos a instância da aplicação Flask.
# __name__ informa ao Flask onde procurar templates e arquivos estáticos.
app = Flask(__name__, template_folder='../templates', 
            static_folder='../static')


# O decorador @app.route define qual URL aciona esta função.
# A rota '/' é a raiz do site — a página inicial.
@app.route("/")
def index():
    """Rota raiz: exibe instruções de como usar a demo."""
    return render_template("index.html")


# O decorador @app.route define a rota dinâmica.
# O trecho <nome> entre < > é um PARÂMETRO VARIÁVEL.
# O Flask captura automaticamente o valor digitado na URL
# e o passa como argumento para a função Python abaixo.
@app.route("/saudacao/<nome>")
def saudacao(nome):
    """
    Rota dinâmica: recebe o parâmetro 'nome' da URL.

    Exemplo: acessar /saudacao/Maria chama esta função
    com nome='Maria'.
    """
    return render_template("saudacao.html", nome=nome)


if __name__ == "__main__":
    # Lê a porta do ambiente (Vercel, etc), padrão 5000
    # serve para garantir que o servidor só inicie quando
    # executamos o script principal (index.py)
    # além de permitir que, localmente, seja iniciado na porta 5000
    # e, em nuvens, a porta seja automaticamente detectada.
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
