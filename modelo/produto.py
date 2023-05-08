from modelo.loja import Loja
from modelo.categoria import Categoria


class Produto:
    def __init__(self, nome: str, loja: Loja, tipo: Categoria):
        self.__nome = nome
        self.__loja = loja
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def loja(self):
        return self.__loja

    @loja.setter
    def loja(self, loja: Loja):
        if isinstance(loja, Loja):
            self.__loja = loja

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: Categoria):
        if isinstance(tipo, Categoria):
            self.__tipo = tipo
