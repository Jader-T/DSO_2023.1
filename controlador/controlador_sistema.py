from tela.tela_sistema import TelaSistema
from controlador.controlador_usuario import ControladorUsuarios


class ControladorSistema:
    
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()
    
    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    def inicializa_sistema(self):
        self.abre_tela()

    #def faz_login(self):
        #self.__abre_tela_login() controle de toda a sessão do #usuário após ele fazer login no sistema
    
    def configura_usuarios(self):
        self.__controlador_usuarios.abre_tela()
        
    def encerra_sistema(self):
        exit(0)
    
    #def abre_tela_login(self):
        #lista_opcoes = {1: self.faz_login, 2: self.configura_usuario}
        
    def abre_tela(self):
        lista_opcoes = {1: self.configura_usuarios, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()