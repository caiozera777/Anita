def soma (n1, n2):
    soma = n1 + n2
    return soma
# +, -, *, /, //, %, **
def subtracao (n1, n2):
    subtracao = n1 - n2
    return subtracao

def multiplicacao (n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

def divisao (n1, n2):
    divisao = n1 / n2
    return divisao

def exponencial (n1, n2):
    exponencial = n1 // n2
    return exponencial

def restodiv (n1, n2):
    restodiv = n1 % n2
    return restodiv

def raizquadrada (n1, n2):
    raizquadrada = n1 ** n2
    return raizquadrada 


soma, subtracao, multiplicacao, divisao, exponencial, restodiv, raizquadrada

n1 = int(input("\n Digite um numero:"))
n2 = int(input("\n Digite o outro numero:"))

print(f"\n a soma entre {n1} e {n2} é {soma(n1, n2)}")


print(f"\n a subtracao entre {n1} e {n2} é {subtracao(n1, n2)}")


print(f"\n a multiplicacao entre {n1} e {n2} é {multiplicacao(n1, n2)} ")


print(f"\n a divisao entre {n1} e {n2} é {divisao(n1, n2)}")







 
    
    
    
    