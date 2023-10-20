nome        = (input('digite seu nome'))
idade       = (input('digite sua idade'))
anoletivo   = (input("digite seu ano letivo"))
materia     = (input("digite sua materia"))
nota1       = float(input("gite sua primeira nota"))
nota2       = float(input('digite sua segunda nota'))
media       = (nota1 + nota2)/2

lista = [ nome, idade, anoletivo, materia, nota1, nota2, media]
print(lista)

if media > 7:
    print("a média é maior que 7.0")
    
elif media > 7:
    print("a média é menor que 7.0")  
    
else:
    print("a média é exatamente 7.0")  
    
poli ="="*20 
print(poli , "média" , poli)     

print(f''' 
      o nome do aluno é : {nome}
      a idade do aluno é : {idade}
      a primeira idade do aluno é : {nota1}
      a segunda nota do aluno é : {nota2}
      ''')
      