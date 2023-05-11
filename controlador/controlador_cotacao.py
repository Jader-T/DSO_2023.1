from modelo.cotacao import Cotacao
from tela.tela_cotacao import TelaCotacao
from random import randint


class ControladorCotacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cotacoes = []
        self.__tela_cotacao = TelaCotacao(self)

    '''Verificar as demais implementações e verificar sobre o ATRIBUTO: CODIGO'''
    def inclui_cotacao(self):
        dados_cotacao = self.__tela_cotacao.pega_dados_cotacao()
        produto = self.__controlador_sistema.controlador_produto.seleciona_produto()
        cotacao = Cotacao(dados_cotacao["preco"], produto, randint(0, 200))
        self.__cotacoes.append(cotacao)

    def lista_cotacao(self):
        for cotacao in self.__cotacoes:
            self.__tela_cotacao.mostra_cotacao({"preco": cotacao.preco,
                                                "nome_produto": cotacao.produto,
                                                "codigo": cotacao.codigo})

    def busca_cotacao_pelo_codigo(self, codigo):
        for cotacao in self.__cotacoes:
            if cotacao.codigo == codigo:
                return cotacao
        else:
            return None

    def seleciona_cotacao(self):
        while True:
            codigo_cotacao = self.__tela_cotacao.pega_codigo_cotacao()
            cotacao = self.busca_cotacao_pelo_codigo(codigo_cotacao)
            if cotacao != None:
                return cotacao

    def abre_tela_cotacao(self):
        lista_opcoes = {1: self.inclui_cotacao, 2: self.lista_cotacao, 3: self.gera_relatorio, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_cotacao.mostra_opcoes_cotacao()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def gera_relatorio(self):
        pass

    def altera_cotacao(self):
        pass

    def rem_cotacao(self):
        pass
