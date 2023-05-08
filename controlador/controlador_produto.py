from modelo.produto import Produto
from tela.tela_produto import TelaProduto


class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto()

    '''Criar as funções do controlador'''

    def inclui_produto(self):
        pass

    def altera_produto(self):
        pass

    def gera_relatorio(self):
        pass


