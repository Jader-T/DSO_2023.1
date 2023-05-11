from modelo.cotacao import Cotacao

class Compra:
    def __init__(self, data_compra: str, cotacao: Cotacao, transportadora: str): #chegou: bool
        self.__data_compra = data_compra
        if (isinstance(cotacao, Cotacao)):
            self.__cotacao = cotacao
        #self.__chegou = chegou
        self.__transportadora = transportadora

    @property
    def data_compra(self):
        return self.__data_compra

    @data_compra.setter
    def data_compra(self, data_compra: str):
        if isinstance(data_compra, str):
            self.__data_compra = data_compra

    @property
    def cotacao(self):
        return self.__cotacao

    @cotacao.setter
    def cotacao(self, cotacao: Cotacao):
        if isinstance(cotacao, Cotacao):
            self.__cotacao = cotacao

    @property
    def transportadora(self):
        return self.__transportadora

    @transportadora.setter
    def transportadora(self, transportadora: str):
        if isinstance(transportadora, str):
            self.__transportadora = transportadora

    #Verificar sobre o atributo chegou