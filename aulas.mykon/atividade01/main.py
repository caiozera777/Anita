from series import Series


lista_series = []

print(' < Seja bem vindo ao Netflix >\n')
print('\t1_ Cadastrar ')
print('\t2_Listar ')
print('\t3 Sair do cistema \n')


Valida = False
while(not Valida):
    opcao = int (input('Escolha uma das opcoes >> '))

    if(opcao == 1):
        series = Series()
        series.nome = input('Digite o nome >>')
        series.sinopse = input('Digite a sinopse >>')
        series.temporadas = input('Digite a quantidade de temporadas >>')
        series.episodios = input('Digite o numero de episodios >>')
        series.duracao = input('Digite a duracao da serie >>')
        series.elenco = input('Digite o elenco >>')
        series.classificacao = input('Digite a classificacao indicativa >>\n')
        lista_series.append(series)
        print('Serie cadastrada com sucesso!!\n')
        

    

    elif(opcao == 2):
        for s  in lista_series:
            print(s)

 
    elif(opcao == 3):
        Valida = True
        print('Você saiu do sistema!!')
 

    else:
        print('Você saiu do sistema!!')

