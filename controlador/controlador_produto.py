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
        for produto in self.__produtos:
            self.__tela_produto.mostra_produto({"nome": produto.nome, "loja": produto.loja.nome, "tipo": produto.tipo})

    def abre_tela_produto(self):
        lista_opcoes = {1: self.inclui_produto, 2: self.lista_produtos, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_produto.mostra_opcoes_produto()]()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def busca_produto_pelo_nome(self, nome):
        for produto in self.__produtos:
            if produto.nome == nome:
                return produto
        else:
            return None

    def seleciona_produto(self):
        while True:
            nome_produto = self.__tela_produto.pega_nome_produto()
            produto= self.busca_produto_pelo_nome(nome_produto)
            if produto != None:
                return produto
