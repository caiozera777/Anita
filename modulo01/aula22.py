n1 = float(input("digite sua nota"))
n2 = float (input("digite sua nota"))
media = (n1 + n2) / 2

if media <=3.0:
    print("voce foi reprovado por unanimidade seu vacilao")
    
elif media <6.0:
    print("voce ainda tem chance de passar, fazendo recuperacao")
    
elif media >=7.0 <8.0:
    print("voce passou mas nao merece parabens, fez sua obrigaçao")
    
elif media >=8.0 <=9.0:
    print("voce foi bem parabens")
    
elif media >9.0:
    print("voce é bagual")
    
else :
    print("sua nota ela nao foi nem ruim para voce ser um mal aluno")
    print("mas ela tambem nao foi regular, sugiro procurar um médico")