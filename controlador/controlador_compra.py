from modelo.cotacao import Cotacao
from tela.tela_compra import TelaCompra


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__compras = []
        self.__tela_compra = TelaCompra

    '''Composição'''
    def inclui_cotacao(self, preco: float, produto: 'Produto'): '''Verificar com o professor sobre isso'''
        pass
    def comprou(self):
        pass

    def gera_relatorio(self):
        pass


