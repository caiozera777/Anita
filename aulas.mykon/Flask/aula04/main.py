from flask import Flask, render_template

class Cerveja:
    def __init__(self , nome, estilo, ibu, abv, graduacao):
        self.nome = nome
        self.estilo = estilo
        self.ibu = ibu
        self.abv = abv
        self.graduacao = graduacao

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cerveja/lista')
def cerveja__lista():

    c1 = Cerveja( 'Kaiser', 'pilsen', 10, 15, 15)
    c2 = Cerveja( 'Skol', 'pilsen', 12, 18, 6)
    
    cerveja_lista = [c1, c2]

    return render_template('cerveja/lista.html' , lista = cerveja_lista)

app.run(debug=True)