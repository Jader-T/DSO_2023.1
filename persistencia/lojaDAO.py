from persistencia.DAO import DAO
from modelo.loja import Loja


class LojaDAO(DAO):
    def __init__(self):
        super().__init__('loja.pkl')

    def add(self, loja: Loja):
        if isinstance(loja, Loja):
            super().add(loja.nome, loja)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key):
        # if isinstance(key):
        return super().remove(key)
