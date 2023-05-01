from modelo.loja import Loja
from tela.tela_loja import TelaLoja

class ControladorLoja:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lojas = []
        self.__tela_loja = TelaLoja(self)

    def inclui_loja(self):
        dados = self.__tela_loja.pega_dados_loja()
        loja = Loja(dados[0], dados[1])
        self.__lojas.append(loja)
