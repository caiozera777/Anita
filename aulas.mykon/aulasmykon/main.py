from usuario_crud import Crudusuario, lista_usuario, cadastrar


crud = Crudusuario()


print('Bem-vindo ao sistema de agendamento')
print('\t1_ Cadastrar usuario')
print('\t2_Listar usuario')

Valida = True
while(not Valida):
    opcao = int (input('Escolha uma das opcoes; '))

if(opcao == 1):
    usuario = Usuario
    usuario.nome = input('Digite o nome >>')
    usuario.sobrenome = input('Digite o sobrenome >>')
    usuario.email = input('Digite o email >>')
    usuario.senha = input('Digite a senha >>')
    cadastrar(nome, sobrenome, email, senha)

    
elif(opcao == 2):
    for u  in lista_usuario:
        print(u)
   # Valida = True
    
else:
    print('Opção incorreta, digite novamente ')
    Valida = False