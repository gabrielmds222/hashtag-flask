from flask import Flask, render_template

app = Flask(__name__)

# Criar a home do site
# Route => gabrielmedsilva/site
@app.route('/')

# Função => O que vai ser exibido na tela

def homepage():
    return render_template('homepage.html')

@app.route('/contatos')

def contatos():
    return render_template('contatos.html')

@app.route('/user/<username>')

def user(username):
    return render_template('usuarios.html', username=username)

# Colocar o site no ar
if __name__ == '__main__':
    app.run(debug=True)