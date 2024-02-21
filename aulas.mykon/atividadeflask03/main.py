from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')


@app.route('/lista')
def listar():
    return render_template('lista.html')


app.run(host='0.0.0.0', port=80, debug=True)