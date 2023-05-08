from modelo.cotacao import Cotacao
from tela.tela_cotacao import TelaCotacao


class ControladorCotacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cotacoes = []
        self.__tela_cotacao  = TelaCotacao(self)

    '''implementar as funções de incluir, alterar e remover, de acordo com as opções na tela_cotacao'''
    def inclui_cotacao(self):
        pass

    def altera_cotacao(self):
        pass

    def rem_cotacao(self):
        pass