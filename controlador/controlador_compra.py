from tela.tela_compra import TelaCompra
from modelo.compra import Compra

class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__compras = []
        self.__tela_compra = TelaCompra

    def inclui_compra(self):
        dados_compra= self.__tela_compra.pega_dados_compra(self)
        cotacao = self.__controlador_sistema.controlador_cotacao.seleciona_cotacao()
        compra = Compra(dados_compra["data"], cotacao, dados_compra["transportadora"])
        self.__compras.append(compra)

    def lista_compra(self):
        for compra in self.__compras:
            self.__tela_compra.mostra_compra({"data": compra.data_compra,
                                              "cotacao:": compra.cotacao,
                                              "transporta": compra.transportadora})

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_compra(self):
        lista_opcoes = {1: self.inclui_compra, 2: self.lista_compra, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_compra.mostra_opcoes_compra(self)]()

    def busca_compra_pela_cotacao(self, cotacao):
        for compra in self.__compras:
            if compra.cotacao.codigo == cotacao.codigo:
                return cotacao
        else:
            return None

    def gera_relatorio(self):
        pass


