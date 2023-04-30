from usuario import Usuario


class PessoaFisica(Usuario):
    def __init__(self, nome: str, fone: int, email: str, cpf: str):
        super().__init__(nome, fone, email)
        
        if isinstance(cpf, str):
            self.__cpf = cpf
            
    @property
    def cpf(self, cpf):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if isinstance (cpf, str):
            self.__cpf = cpf        