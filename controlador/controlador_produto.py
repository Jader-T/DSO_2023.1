from modelo.produto import Produto
from tela.tela_produto import TelaProduto


class ControladorProduto:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__produtos = []
        self.__tela_produto = TelaProduto(self)

    def inclui_produto(self):
        dados_produtos = self.__tela_produto.pega_dados_produto()
        produto = Produto(dados_produtos["nome"], dados_produtos["tipo"])
        self.__produtos.append(produto)
        self.__tela_produto.mostra_msg("\n***Produto adicionado!***\n")

    def lista_produtos(self):
        produtos_listados = []
        if len(self.__produtos) == 0:
            self.__tela_produto.mostra_msg("\nNão há produtos cadastrados!\n")
            return
        else:
            for produto in self.__produtos:
                produtos_listados.append({"nome": produto.nome, "tipo": produto.tipo})
            if produtos_listados:
                self.__tela_produto.mostra_produto(produtos_listados)

    def abre_tela_produto(self):
        lista_opcoes = {1: self.inclui_produto, 2: self.lista_produtos,
                        3: self.altera_produto, 0: self.retornar_sistema}
        while True:
            lista_opcoes[self.__tela_produto.mostra_opcoes_produto()]()

    def retornar_sistema(self):
        self.__controlador_sistema.abre_tela()

    def retornar_cotacao(self):
        self.__controlador_sistema.controlador_cotacao.abre_tela_cotacao()

    def busca_produto_pelo_nome(self, nome):
        for produto in self.__produtos:
            if produto.nome == nome:
                return produto
        else:
            return None

    def seleciona_produto(self):
        while True:
            nome_produto = self.__tela_produto.pega_nome_produto()
            produto = self.busca_produto_pelo_nome(nome_produto)
            if produto is not None:
                return produto
            else:
                self.__tela_produto.mostra_msg("\nAtenção! O produto informado não existe "
                                               "favor cadastrar ou listar produtos no "
                                               "menu de produtos\n")
                break

    def altera_produto(self):
        self.lista_produtos()
        nome_produto = self.__tela_produto.pega_nome_produto()
        produto = self.busca_produto_pelo_nome(nome_produto)
        novos_dados_produto = self.__tela_produto.pega_dados_produto()

        if produto is None:
            self.__tela_produto.mostra_msg("Produto não encontrado!")
            return


        if not isinstance(produto, Produto):
            self.__tela_produto.mostra_msg("Não é possível alterar o tipo do produto!")
            return
        produto.nome = novos_dados_produto["nome"]
        produto.tipo = novos_dados_produto["tipo"]

        self.__tela_produto.mostra_msg("\nProduto alterado com sucesso!\n")
        self.lista_produtos()
