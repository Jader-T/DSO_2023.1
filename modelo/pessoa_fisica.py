from modelo.usuario import Usuario


class PessoaFisica(Usuario):
    def __init__(self, nome: str, fone: int, email: str, cpf: str, senha: str):
        super().__init__(nome, fone, email, senha)
        
        if isinstance(cpf, str):
            self.__cpf = cpf
            
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, str):
            self.__cpf = cpf
