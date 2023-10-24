nome = input("digite seu nome")
viagem1 = input("digite o local de sua primeira viagem")


viagem2 = input("digite o local de sua segunda viagem")


viagem3 = input("digite o local de sua terceira viagem")


viagem4 = input("digite o local de sua quarta viagem")


viagem5 = input("digite o local de sua quinta viagem")


viagem6 = input("digite o local de sua quinta viagem")

lista = [viagem1, viagem2, viagem3, viagem4, viagem5, viagem6]
print(lista)

poli = "*"*20

from random import choice, shuffle
shuffle(lista)
sorteio = choice(lista)

if sorteio ==viagem1:
    print(f"seu destino é : {viagem1}")
    
elif sorteio ==viagem2:
    print(f"seu destino é : {viagem2}")
    
elif sorteio ==viagem3:
    print(f"seu destino é : {viagem3}")
    
elif sorteio ==viagem4:
    print(f"seu destino é : {viagem4}")
    
elif sorteio ==viagem5:
    print(f"seu destino é : {viagem5}")
    
elif sorteio ==viagem6:
    print(f"seu destino é : {viagem6}")


print(poli, "primeira viagem", poli, "\n")
print(f"Obrigado {nome} por ter escolhido nossa agência,APROVEITE SUA VIAGEM!!")