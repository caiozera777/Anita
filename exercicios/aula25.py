nome1 = input("digite seu nome")
idade1 = float(input("dgite uma idade entre 18 até 50 anos"))

nome2 = input("digite seu nome")
idade2 = float(input("dgite uma idade entre 18 até 50 anos"))

nome3 = input("digite seu nome")
idade3 = float(input("dgite uma idade entre 18 até 50 anos"))

media_idade = (idade1 + idade2 + idade3)/3
idade = (idade1, idade2, idade3)
nomes = [nome1, nome2, nome3]

categoria = None

if media_idade < 18:
    ctegoria = "menor de 18"
    
elif media_idade >= 18 <30:
    categoria = "entre 18 e 29"
    
elif media_idade >= 30 <40:
    categoria = "entre 30 e 39"
    
elif media_idade >=40 <=50:
    categoria = "entre 40 e 50"
    
print("A média das idades é", categoria)

print("A lista de nomes é ", nomes)

print("A lista de idade é", idade )

print("A categoria das idades dos usúarios são", categoria)