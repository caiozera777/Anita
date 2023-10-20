nome = (input("digite seu nome"))
altura = float(input("digite sua altura em metros"))
peso = float(input("digite seu peso em quilogramas"))

imc = peso/(altura**2)

categoria = None

if imc < 18.5:
    categoria = "abaixo de peso"
    
elif imc >= 24.9:
    categoria = "peso normal"
    
elif imc >= 20.9:
    categoria = "sobrepeso"
    
elif imc >= 30:
    categoria = "obeso"
    
print("Olá", nome, "segundo os calculos do seu imc você está", categoria)