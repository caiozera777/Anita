class Series:
    nome                = ''
    sinopse             = ''
    temporadas          =  ''
    episodios           = ''
    duracao             = ''
    elenco              = ''
    classificacao       = ''
    
    
    
    
    
    def __str__(self) -> str:
        return f'{self.nome} - {self.sinopse} - {self.temporadas} - {self.episodios} - {self.duracao} - {self.elenco} - {self.classificacao}'