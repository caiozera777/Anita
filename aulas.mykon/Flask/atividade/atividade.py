from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Seja Bem Vindo !'


@app.route('/pessoa')
def pessoa():
    return 'Bem Vindo ao modulo de pessoas'

app.run(host='0.0.0.0', port=8080, debug=True)