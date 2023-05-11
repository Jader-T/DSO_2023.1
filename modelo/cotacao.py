from modelo.produto import Produto


class Cotacao:
    def __init__(self, preco: float, produto: Produto, codigo: int):
        self.__preco = preco
        if (isinstance(produto, Produto)):
            self.__produto = produto
        self.__codigo = codigo

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco: float):
        if isinstance(preco, float):
            self.__preco = preco

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto: Produto):
        if isinstance(produto, Produto):
            self.__produto = produto
