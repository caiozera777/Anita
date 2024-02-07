from pessoa import Pessoa
from endereco import Endereco

nome = 'jorgin'
sobrenome = 'silva'
idade = 69
endereco = Endereco('Rua do vini','6969','ao lado da casa do vini', 'salto', 'blumenau')

p1 = Pessoa(nome, sobrenome, idade, endereco)    

print(p1)