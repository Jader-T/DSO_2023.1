

class Loja:
    def __init__(self, nome: str, site: str):
        self.__nome = nome
        self.__site = site

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
