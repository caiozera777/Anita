<<<<<<< HEAD
var = 'sim'

#lover()transforma a string em minusculo
# upper()transforma a string toda em minusculo
#capitalize()transforma a primeira em minusculo

while var,capitalize() == 'Sim'
    n1 = int(input("digite um numero"))
    n2 = int(input("digite um numero"))
    soma = n1 + n2
    print(f"o primeiro numero é {n1}\n o segundo numero digitado é {n2}\n a soma é {soma}")
    
    print(f"deseja fazer um novo calculo?")
    var = int(input("digite 1 para continuar?\nDigite 0 para sair"))
    
print("voce saiu do sistema")

=======
from datetime import datetime
from time import sleep
situacao = "Reprovado"
while situacao.capitalize() == "Reprovado":
# Bloco 1 saudação
    hora = datetime.now(tz=None)
    if hora.hour >=5 and hora.hour <13:
        print(" Bom Dia")
    elif hora.hour >=13 and hora.hour <18:
        print("Boa Tarde")
    else:
        print(" Boa Noite") 
# Bloco 2
    nome = input(" digite seu nome")
    sobrenome = input(" digite seu sobrenome")
    idade = int(input(" digite sua idade"))
    listaNotas = []

#Bloco 3
    for i in range(1, 7):
        nota = float(input(f" Digite a nota {i} >> "))
        listaNotas.append(nota)
    media = sum( listaNotas) / len(listaNotas)

# Bloco 4
    if media < 7.0:
        situacao = "Rerpovado"
        print(f"Ola {nome} infelismente voce foi reprovadocom media {media}")
        print(" tente novamente e tenha boa sorte")
    elif media >=7.0:
        situacao = "Aprovado"
        for i in range(10):
            sleep(1)
            print("*")
        print("parabens !!")
        print(f"{nome}voce foi Aprovado e ira para um novo desafio, sua media foi {media}")
    Aluno = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade,
        "Notas": listaNotas,
        "situacao": situacao,
    }

    print("voce deseja receber todas as informações do aluno?")
    var = input("Sim\nNao\n >>")

    if var.capitalize() == "Sim":
        print(f'''
{Aluno['nome']}
{Aluno['sobrenome']}
{Aluno["idade"]}
{Aluno['Notas']}
{Aluno['situacao']}

''')
>>>>>>> 0bee2c9f73a3565cc6b1aa5bf2e77989211d1475
