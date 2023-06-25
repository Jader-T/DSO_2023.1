from persistencia.DAO import DAO
from modelo.endereco_filial import EnderecoFilial


class EnderecoDAO(DAO):
    def __init__(self):
        super().__init__('endereco_filial.pkl')

    def add(self, endereco_filial: EnderecoFilial):
        if isinstance(endereco_filial, EnderecoFilial):
            super().add(endereco_filial.pais, endereco_filial)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key):
        # if isinstance(key):
        return super().remove(key)
