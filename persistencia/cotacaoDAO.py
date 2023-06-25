from persistencia.DAO import DAO
from modelo.cotacao import Cotacao


class CotacaoDAO(DAO):
    def __init__(self):
        super().__init__('cotacao.pkl')

    def add(self, cotacao: Cotacao):
        if isinstance(cotacao, Cotacao):
            super().add(cotacao.codigo, cotacao)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key):
        # if isinstance(key):
        return super().remove(key)
