from modelo.cotacao import Cotacao
from tela.tela_cotacao import TelaCotacao
from random import randint


class ControladorCotacao:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__cotacoes = []
        self.__tela_cotacao = TelaCotacao(self)

    def inclui_cotacao(self):
        dados_cotacao = self.__tela_cotacao.pega_dados_cotacao()
        produto = self.__controlador_sistema.controlador_produto.seleciona_produto()
        if produto is not None:
            cotacao = Cotacao(dados_cotacao["preco"], produto, randint(0, 200))
            self.__cotacoes.append(cotacao)
            self.__tela_cotacao.mostra_msg("\n***Cotação incluída***\n")

    def lista_cotacao(self):
        if len(self.__cotacoes) == 0:
            self.__tela_cotacao.mostra_msg("\nNão há cotações cadastradas!\n")
            return
        else:
            for cotacao in self.__cotacoes:
                self.__tela_cotacao.mostra_cotacao({"preco": cotacao.preco,
                                                    "nome_produto": cotacao.produto.nome,
                                                    "loja": cotacao.produto.loja.nome,
                                                    "codigo": cotacao.codigo})

    def busca_cotacao_pelo_codigo(self, codigo):
        for cotacao in self.__cotacoes:
            if cotacao.codigo == codigo:
                return cotacao
        else:
            return None

    def busca_cotacao_pelo_nome(self, produto_cotacao):
        for cotacao in self.__cotacoes:
            if cotacao.produto.nome == produto_cotacao:
                return cotacao
        else:
            return None

    def seleciona_cotacao(self):
        while True:
            codigo_cotacao = int(self.__tela_cotacao.pega_codigo_cotacao())
            dados = self.busca_cotacao_pelo_codigo(codigo_cotacao)
            if dados is not None:
                return dados
            else:
                self.__tela_cotacao.mostra_msg("\nEssa cotação não existe! favor listar "
                                               "ou cadastrar cotações no menu de cotações\n")
                break

    def abre_tela_cotacao(self):
        lista_opcoes = {1: self.inclui_cotacao, 2: self.lista_cotacao, 3: self.remover_cotacao,
                        4: self.gera_relatorio, 0: self.retornar_sistema, 10: self.retornar_compras}
        while True:
            lista_opcoes[self.__tela_cotacao.mostra_opcoes_cotacao()]()

    def retornar_sistema(self):
        self.__controlador_sistema.abre_tela()

    def retornar_compras(self):
        self.__controlador_sistema.controlador_compra.abre_tela_compra()

    def remover_cotacao(self):
        produto_cotacao = self.__tela_cotacao.pega_nome_cotacao()
        cotacao = self.busca_cotacao_pelo_nome(produto_cotacao)
        if cotacao is not None:
            self.__cotacoes.remove(cotacao)
            self.__tela_cotacao.mostra_msg("\n***Cotação removida!***\n")
        else:
            self.__tela_cotacao.mostra_msg("\nCotação informada não existe\n")

    def remover_cotacao(self):
        produto_cotacao = self.__tela_cotacao.pega_nome_cotacao()
        cotacao = self.busca_cotacao_pelo_nome(produto_cotacao)
        if cotacao is not None:
            self.__cotacoes.remove(cotacao)
            self.__tela_cotacao.mostra_msg("\n***Cotação removida!***\n")
        else:
            self.__tela_cotacao.mostra_msg("\nCotação informada não existe\n")

    def gera_relatorio(self):
        valor_minimo = self.__tela_cotacao.pega_valor_inicial()
        valor_maximo = self.__tela_cotacao.pega_valor_final()
        cotacoes_filtradas = []

        for cotacao in self.__cotacoes:
            if valor_minimo <= cotacao.preco <= valor_maximo:
                cotacoes_filtradas.append(cotacao)

        if len(cotacoes_filtradas) == 0:
            self.__tela_cotacao.mostra_msg("\nNão há cotacoes registradas dentro da faixa de valor selecionada!\n")
            return
        else:
            for cotacao in cotacoes_filtradas:
                self.__tela_cotacao.mostra_relatorio({"preco": cotacao.preco,
                                                    "nome_produto": cotacao.produto.nome,
                                                    "loja": cotacao.produto.loja.nome,
                                                    "codigo": cotacao.codigo})