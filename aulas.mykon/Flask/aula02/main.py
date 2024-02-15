#uma rota chama a execução de um método

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('pessoa')
def pessoa():
    return render_template('pessoa.h')


app.run(debug=True)