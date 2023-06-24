

class EnderecoFilial:
    def __init__(self, pais: str, estado: str):
        self.__pais = pais
        self.__estado = estado

    @property
    def pais(self):
        return self.__pais

    @property
    def estado(self):
        return self.__estado
