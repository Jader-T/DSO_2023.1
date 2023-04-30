from usuario import Usuario


class PessoaJurica(Usuario):
    def __init__(self, nome: str, fone: int, email: str, cnpj: str):
        super().__init__(nome, fone, email)
        if isinstance(cnpj, str):
            self.__cnpj = cnpj
    
    @property
    def cnpj(self, cnpj):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        if isinstance (cnpj, str):
            self.__cnpj = cnpj