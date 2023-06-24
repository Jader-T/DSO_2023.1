from modelo.loja import Loja
from tela.tela_loja import TelaLoja


class ControladorLoja:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lojas = []
        self.__tela_loja = TelaLoja(self)

    ''''@property
    def enderecos(self):
        return self.__enderecos'''

    def inclui_loja(self):
        dados_loja = self.__tela_loja.pega_dados_loja(self)
        loja = Loja(dados_loja["nome"], dados_loja["site"])
        self.__lojas.append(loja)
        self.__tela_loja.mostra_msg("\n***Loja adicionada!***\n")
        return None

    def lista_lojas(self):
        lojas_listadas = []
        if len(self.__lojas) == 0:
            self.__tela_loja.mostra_msg("\nNão há lojas cadastradas!\n")
            return
        else:
            '''for loja in self.__lojas:
                self.__tela_loja.mostra_loja({"nome": loja.nome, "site": loja.site})'''
            for loja in self.__lojas:
                lojas_listadas.append({"nome": loja.nome, "site": loja.site})
            if lojas_listadas:
                self.__tela_loja.mostra_loja(lojas_listadas)

    def add_endereco(self):
        loja = self.seleciona_loja()
        if loja is not None:
            dados_endereco = self.__tela_loja.pega_dados_endereco()
            Loja.incluir_endereco(loja, dados_endereco["pais"], dados_endereco["estado"])
            self.__tela_loja.mostra_msg("\nEndereço adicionado!\n")

    def lista_enderecos(self):
        enderecos_listados = []
        loja = self.seleciona_loja()
        for enderecos in loja.enderecos_filial:
            enderecos_listados.append({"pais": enderecos.pais, "estado": enderecos.estado})
        if enderecos_listados:
            self.__tela_loja.mostra_enderecos(enderecos_listados)

    def retornar_sistema(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela_loja(self):
        lista_opcoes = {1: self.inclui_loja, 2: self.lista_lojas, 3: self.add_endereco,
                        4: self.lista_enderecos, 0: self.retornar_sistema}
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
