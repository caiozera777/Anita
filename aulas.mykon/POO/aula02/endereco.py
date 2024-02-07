class Endereco:
    def __init__(self, rua, numero, complemento, bairo, cidade):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairo = bairo
        self.cidade = cidade


    def __str__(self):
        return f'{self.rua} - {self.numero} - {self.complemento} - {self.bairo} - {self.cidade}'