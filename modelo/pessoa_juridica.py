from modelo.usuario import Usuario


class PessoaJuridica(Usuario):
    def __init__(self, nome: str, fone: int, email: str, cnpj: str, senha: str):
        super().__init__(nome, fone, email, senha)
        
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        if isinstance (cnpj, str):
            self.__cnpj = cnpj