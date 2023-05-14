from modelo.cotacao import Cotacao


class Compra:
    def __init__(self, data_compra: str, prazo_entrega: str, chegou: bool):
        self.__data_compra = data_compra
        if isinstance(dados, Cotacao):
            self.__dados = dados
        self.__transportadora = transportadora

    @property
    def data_compra(self):
        return self.__data_compra

    @data_compra.setter
    def data_compra(self, data_compra: str):
        if isinstance(data_compra, str):
            self.__data_compra = data_compra

    @property
    def dados(self):
        return self.__dados

    @dados.setter
    def dados(self, dados: Cotacao):
        if isinstance(dados, Cotacao):
            self.__dados = dados

    @property
    def transportadora(self):
        return self.__transportadora

    @transportadora.setter
    def transportadora(self, transportadora: str):
        if isinstance(transportadora, str):
            self.__transportadora = transportadora
