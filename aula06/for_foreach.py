lista = ['caio', 'fernando']

for p in lista:
    print(p)
    
    
for n in range(0, (lista)):
    print(lista(n))   #for incremental tradicional
    
#remove  
lista.remove('caio')
print(lista)

#pop
dado = lista.pop(0)
print(lista)
print('Dado removido: '+ dado)

#del
del lista(1)
print(lista)