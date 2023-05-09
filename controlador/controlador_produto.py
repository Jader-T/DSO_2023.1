from modelo.produto import Produto
from tela.tela_produto import TelaProduto

class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto(self)

    '''Criar as funções do controlador'''
    def inclui_produto(self):
        dados_produtos = self.__tela_produto.pega_dados_produto()
        loja = self.__controlador_sistema.controlador_loja.seleciona_loja()
        produto = Produto(dados_produtos["nome"], loja, dados_produtos["tipo"])
        self.__produtos.append(produto)

    def lista_produtos(self):
        pass

    def altera_produto(self):
        pass

    def abre_tela_produto(self):
        lista_opcoes = {1: self.inclui_produto, 2: self.lista_produtos, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_produto.mostra_opcoes_produto()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()


