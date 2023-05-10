from modelo.cotacao import Cotacao

class Compra:
    def __init__(self, data_compra: str, prazo_entrega: str, chegou: bool):
        self.__data_compra = data_compra
        self.__prazo_entrega = prazo_entrega
        self.__chegou = chegou




