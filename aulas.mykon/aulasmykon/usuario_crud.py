from usuario import Usuario

lista_usuario = []
 
def cadastrar(self, nome, sobrenome, email, senha):
    usuario = Usuario
    usuario.nome = nome
    usuario.sobrenome = sobrenome
    usuario.email = email
    usuario.senha = senha
    self.lista_usuario.append(usuario)
    
def listar(self):
    return self.lista_usuario