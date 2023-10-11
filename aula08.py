#operadores relacionais sao um conjunto de simbolos
validador : bool
validador = True
idade = int(input("digite sua idade >> "))

#igual a 18
validador = (idade == 18)
print(f"a idade é igual a 18? {validador}")
#diferente de 18
validador = (idade != 18)
print(f"a idade é diferente de 18? {validador}")

validador = ( idade > 18)
print(f"a idade é maior de 18? {validador}")

validador = ( idade < 18)
print(f"a idade é menor que 18? {validador}")

validador = (idade >= 18)
print(f"a idade é maior ou igual a 18? {validador}")

validador = (idade <= 18)
print(f"a idade é menor ou igula a 18? {validador}")