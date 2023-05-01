from modelo.produto import Produto


class Cotacao:
    def __init__(self, preco: float, produto: Produto):
        self.__preco = preco
        self.__produto = produto

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

