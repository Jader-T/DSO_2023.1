from persistencia.DAO import DAO
from modelo.compra import Compra


class CompraDAO(DAO):
    def __init__(self):
        super().__init__('compra.pkl')

    def add(self, compra: Compra):
        if isinstance(compra, Compra):
            super().add(compra.dados.codigo, compra)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key):
        # if isinstance(key):
        return super().remove(key)
