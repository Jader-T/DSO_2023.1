class Categoria:
    def __init__(self, tipo: str, opcoes: enumerate):
        if isinstance (tipo, str):
            self.__tipo = tipo
        if isinstance (opcoes, enumerate):
            self.__opcoes = opcoes
            
    @property
    def tipo(self, tipo):
        return self.__fone        
    @property
    def opcoes(self, opcoes):
        return self.__email
    
    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, str):
            self.__nome = tipo
    @opcoes.setter
    def opcoes(self, novas_opcoes):
        if not isinstance (novas_opcoes, (list, tuple)):
            raise ValueError("opcoes deve ser uma sequência de valores")
        self.__opcoes = list(enumerate(novas_opcoes))
            