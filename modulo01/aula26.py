n1 = int(input("digite o numero de vezes que deseja pedir a nota de um aluno"))
lista = []


for i in range(n1):
    nota = float(input("digite sua nota :"))
    lista.append(nota)

media = sum(lista) / len(lista)
    
print(media)

