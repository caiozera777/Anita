n1 = input('digite seu nome')
n2 = input('digite seu nome')
n3 = input('digite seu nome')
n4 = input('digite seu nome')
n5 = input('digite seu nome')
n6 = input('digite seu nome')

lista = [n1, n2, n3, n4, n5, n6]

from random import choice, shuffle

shuffle(lista)
sorteio = choice(lista)
poli = "*"*20


if sorteio ==n1:
    print(f"o nome sorteado foi {n1}")
    
elif sorteio ==n2:
    print(f"o nome sortedo foi {n2}")

elif sorteio ==n3:
    print(f"o nome sortedo foi {n3}")
    
elif sorteio ==n4:
    print(f"o nome sortedo foi {n4}")
    
elif sorteio ==n5:
    print(f"o nome sortedo foi {n5}")
    
elif sorteio ==n6:
    print(f"o nome sortedo foi {n6}")
    
print(poli, "trimania de 2024", poli, "\n")
print(f"parabens {sorteio} voce ganhou 500 milhoes de reais")