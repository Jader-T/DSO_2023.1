from persistencia.DAO import DAO
from modelo.produto import Produto

class ProdutoDAO(DAO):
    def __init__(self):
        super().__init__('produto.pkl')

    def add(self, produto: Produto):
        if isinstance(produto, Produto):
            super().add(produto.nome, produto)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key):
        # if isinstance(key):
        return super().remove(key)
