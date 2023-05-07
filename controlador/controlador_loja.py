from modelo.loja import Loja
from tela.tela_loja import TelaLoja
from modelo.endereco_filial import EnderecoFilial


class ControladorLoja:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lojas = []
        self.__tela_loja = TelaLoja()
        self.__enderecos = []

    @property
    def enderecos(self):
        return self.__enderecos

    def inclui_loja(self):
        dados_loja = self.__tela_loja.pega_dados_loja()
        loja = Loja(dados_loja["nome"], dados_loja["site"])
        self.__lojas.append(loja)

    def lista_lojas(self):
        for loja in self.__lojas:
            self.__tela_loja.mostra_loja({"nome": loja.nome, "site": loja.site})

    def add_endereco(self, pais: str = "", estado: str = ""):
        self.__enderecos.append(EnderecoFilial(pais, estado))

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_loja(self):
        lista_opcoes = {1: self.inclui_loja, 2: self.lista_lojas, 0: self.retornar}
        while True:
            lista_opcoes[self.__tela_loja.mostra_opcoes_loja()]()
