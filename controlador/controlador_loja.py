from modelo.loja import Loja
from tela.tela_loja import TelaLoja
from modelo.endereco_filial import EnderecoFilial


class ControladorLoja:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lojas = []
        self.__tela_loja = TelaLoja(self)
        self.__enderecos = []

    @property
    def enderecos(self):
        return self.__enderecos

    def inclui_loja(self):
        dados_loja = self.__tela_loja.pega_dados_loja(self)
        loja = Loja(dados_loja["nome"], dados_loja["site"])
        self.__lojas.append(loja)
        self.__tela_loja.mostra_msg("\n***Loja adicionada!***\n")

    def lista_lojas(self):
        if len(self.__lojas) == 0:
            self.__tela_loja.mostra_msg("\nNão há lojas cadastradas!\n")
            return
        else:
            for loja in self.__lojas:
                self.__tela_loja.mostra_loja({"nome": loja.nome, "site": loja.site})

    def add_endereco(self, pais: str = "", estado: str = ""):
        self.__enderecos.append(EnderecoFilial(pais, estado))

    def retornar_sistema(self):
        self.__controlador_sistema.abre_tela()

    def retornar_produto(self):
        self.__controlador_sistema.controlador_produto.abre_tela_produto()

    def abre_tela_loja(self):
        lista_opcoes = {1: self.inclui_loja, 2: self.lista_lojas, 3: self.inclui_endereco,
                        0: self.retornar_sistema, 10: self.retornar_produto}
        while True:
            lista_opcoes[self.__tela_loja.mostra_opcoes_loja(self)]()

    def busca_loja_pelo_nome(self, nome):
        for loja in self.__lojas:
            if loja.nome == nome:
                return loja
        else:
            return None

    def seleciona_loja(self):
        while True:
            nome_loja = self.__tela_loja.pega_nome_loja()
            loja = self.busca_loja_pelo_nome(nome_loja)
            if loja is not None:
                return loja
            else:
                self.__tela_loja.mostra_msg("\nAtenção! Loja não existente, favor cadastrar "
                                            "ou listar lojas no menu lojas\n")
                break

    def inclui_endereco(self):
        dados_endereco = self.__tela_loja.pega_dados_endereco()
        self.__enderecos.append(EnderecoFilial(dados_endereco["pais"], dados_endereco["estado"]))