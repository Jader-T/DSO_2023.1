

class Produto:
    def __init__(self, nome: str, tipo: str):
        self.__nome = nome
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        if isinstance(tipo, str):
            self.__tipo = tipo
