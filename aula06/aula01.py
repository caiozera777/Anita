#procedimento
def boas_vindas():
    print("bem-vindo ao sistema soma")
    
# função
#responsabilidade unica - uma funcao deve fazer apenas uma coisa
#ter apenas uma responsabilidade - ajuda no reaproveitamento de codigo

def pega_nome():
    nome = input('Digite seu nome')
    return nome

def saudacao(nome):
    print(f'olá, {nome}')
    
boas_vindas()
nome2 = pega_nome()
saudacao(nome2)