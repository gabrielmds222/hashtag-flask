from flask import Flask

app = Flask(__name__)

# Criar a home do site
# Route => gabrielmedsilva/site
@app.route('/')

# Função => O que vai ser exibido na tela

def homepage():
    return "Home do site, teste do debug oppa"

@app.route('/contatos')

def contatos():
    return "<p>Contatos do site:</p> <p>gabrielmedsilva@outlook.com</p>"
# Colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)