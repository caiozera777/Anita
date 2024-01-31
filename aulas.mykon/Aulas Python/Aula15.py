
idadeteste = input("Digite a sua idade: ")

idade = int(idadeteste)

#idade = 70

if idade > 18 and idade < 60:
    print("Você é adulto")
elif idade < 18 and idade > 12:
    print("Você é adolescente")
elif idade < 12:
    print("Você é uma criança")
elif idade >= 18:
    print("Você tem 18 anos")
else:
    print("Você é idoso")

#if
#elif
#else


