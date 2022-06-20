from flask import Flask

app = Flask(__name__)

# Criar a home do site
# Route => gabrielmedsilva/site
@app.route('/')

# Função => O que vai ser exibido na tela

def homepage():
    return "Home do site"
# Colocar o site no ar
app.run()