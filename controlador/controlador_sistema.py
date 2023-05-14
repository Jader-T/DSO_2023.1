from tela.tela_sistema import TelaSistema
from controlador.controlador_usuario import ControladorUsuarios
from controlador.controlador_loja import ControladorLoja
from controlador.controlador_produto import ControladorProduto
from controlador.controlador_cotacao import ControladorCotacao
from controlador.controlador_compra import ControladorCompra

class ControladorSistema:
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_loja = ControladorLoja(self)
        self.__controlador_produto = ControladorProduto(self)
        self.__controlador_cotacao = ControladorCotacao(self)
        self.__controlador_compra = ControladorCompra(self)

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_loja(self):
        return self.__controlador_loja

    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_cotacao(self):
        return self.__controlador_cotacao

    @property
    def controlador_compra(self):
        return self.__controlador_compra

    def inicializa_sistema(self):
        self.abre_tela()

    #def faz_login(self):
        #self.__abre_tela_login() controle de toda a sessão do #usuário após ele fazer login no sistema
    
    def configura_usuarios(self):
        self.__controlador_usuarios.abre_tela()

    def configura_loja(self):
        self.__controlador_loja.abre_tela_loja()

    def configura_produto(self):
        self.__controlador_produto.abre_tela_produto()

    def configura_compra(self):
        self.__controlador_compra.abre_tela_compra()

    def configura_cotacao(self):
        self.__controlador_cotacao.abre_tela_cotacao()

    def encerra_sistema(self):
        exit(0)
    
    #def abre_tela_login(self):
        #lista_opcoes = {1: self.faz_login, 2: self.configura_usuario}
        
    def abre_tela(self):
        lista_opcoes = {1: self.configura_usuarios, 2: self.configura_loja, 3: self.configura_produto,
                        4: self.configura_cotacao, 5: self.configura_compra, 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
