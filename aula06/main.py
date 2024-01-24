from crud_pessoa import create, read_all, read_by_id, update

print(create('joão', 'juvenal', 57))
print(create('maria', 'isadora', 45))
print(create('caio', 'matheus', 15))

lista = read_all()
for p in lista:
   print (p)
    
p = read_by_id(3)
print (p)
pessoa_alterada = {'id':3, 'nome':'Tonho', 'sobrenome': 'Da lua', 'idade': 98}
update(pessoa_alterada)

print('Dados com a alteração')
lista = read_all()
for p in lista:
    print(p)