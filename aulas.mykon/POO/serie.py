class Series:
    nome            = ''
    sinopse         = ''
    temporadas      = 0
    episodios       = 0
    duracao         = ''
    elenco          = ''
    classificacao   = ''
    
    
    def __init__(self, nome, sinopse):
        print('Chamando o metodo construtor')
        self.nome = nome
        self.sinopse = sinopse
    
    def __str__(self):
        return f'nome: {self.nome} - sinopse: {self.sinopse}'