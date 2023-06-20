from modelo.endereco_filial import EnderecoFilial


class Loja:
    def __init__(self, nome: str, site: str):
        self.__nome = nome
        self.__site = site
        self.__endereco_filial = []

    @property
    def enderecos_filial(self):
        return self.__endereco_filial

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if isinstance(nome, str):
            self.__nome = nome

    @property
    def site(self):
        return self.__site

    @site.setter
    def site(self, site: str):
        if isinstance(site, str):
            self.__nome = site

    def incluir_endereco(self, pais, estado):
        self.__endereco_filial.append(EnderecoFilial(pais, estado))
