#Flask é uma biblioteca do Python, para auxiliar na criação do sistema WEB
#Framework alternativo ao flask = Django e Fast
#Biblioteca é um conjunto de classes metodos e funcionalidadespara auxiliar na criação de algo
#Framework = é um conjunto de bibliotecas que auxiliam na criação de uma funcionalidade
#PIP = repositorio de biblioteca. Pacotes e Frameworks Python = https://pypi.org
#instalação do flask = 
#  /  é o endereço raiz(inicio),a rota inicial de um site ou sistema linux
#endereço da minha maquina = localhost / 127.0.0.1
#porta é por onde libera a entrada para uma  determinada aplicação na sua maquina
#a porta padrão de um site é 80
# o modo de debug ativa o recaregamento automatico e melhora os logs




from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Olá'


app.route('/pessoa')
def pessoa():
    return 'pagina pessoa'

app.run(host='0.0.0.0', port=80, debug=True)
