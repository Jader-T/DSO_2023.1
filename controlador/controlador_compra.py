import datetime

from tela.tela_compra import TelaCompra
from modelo.compra import Compra
import time
from persistencia.compraDAO import CompraDAO


class ControladorCompra:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        #self.__compras = []
        self.__tela_compra = TelaCompra(self)
        self.__compra_DAO = CompraDAO()

    @property
    def compras(self):
        return self.__compra_DAO.get_all()

    def inclui_compra(self):
        dados_compra = self.__tela_compra.pega_dados_compra(self)
        dados = self.__controlador_sistema.controlador_cotacao.seleciona_cotacao()
        if dados is not None:
            compra = Compra(dados_compra["data"], dados, dados_compra["transportadora"])
            self.__compra_DAO.add(compra)
            self.__tela_compra.mostra_msg("\n***Compra registrada!!!***\n")

    def lista_compra(self):
        compras_listadas = []
        for compra in self.__compra_DAO.get_all():
            compras_listadas.append({"data": compra.data_compra, "dados_codigo": compra.dados.codigo,
                                     "dados_produto": compra.dados.produto.nome, "dados_preco": compra.dados.preco,
                                     "dados_loja": compra.dados.loja.nome, "transportadora": compra.transportadora})
        if compras_listadas:
            self.__tela_compra.mostra_compra(compras_listadas)
        else:
            self.__tela_compra.mostra_msg("Compra não encontrada")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def gera_relatorio(self):
        data_inicial = self.__tela_compra.pega_data_inicial()
        data_final = self.__tela_compra.pega_data_final()

        compras_filtradas = []

        for compra in self.__compras:
            data_compra = datetime.datetime.strptime(compra.data_compra, '%d/%m/%Y')
            if data_inicial <= data_compra <= data_final:
                compras_filtradas.append({"data": compra.data_compra,
                                                "dados_codigo": compra.dados.codigo,
                                                "dados_produto": compra.dados.produto.nome,
                                                "dados_preco": compra.dados.preco,
                                                "transportadora": compra.transportadora})

        if len(compras_filtradas) == 0:
            self.__tela_compra.mostra_msg("\nNão há compras registradas no período selecionado!\n")
        else:
            self.__tela_compra.mostra_relatorio(compras_filtradas)

    def abre_tela_compra(self):
        lista_opcoes = {1: self.inclui_compra, 2: self.lista_compra, 3: self.gera_relatorio, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_compra.mostra_opcoes_compra(self)]()

    def busca_compra_pela_cotacao(self, dados):
        for compra in self.__compra_DAO.get_all():
            if compra.dados.codigo == dados.codigo:
                return dados
        else:
            return None
