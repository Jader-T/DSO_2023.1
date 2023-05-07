from tela.tela_sistema import TelaSistema
from controlador.controlador_usuario import ControladorUsuários


class ControladorSistema:
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuários
        self.__tela_sistema = TelaSistema
    
    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    def inicializa_sistema(self):
        self.abre_tela()
    #controle de toda a sessão do usuário após ele fazer login no sistema
    def faz_login(self):
        pass #finalizar
    
    def inclui_usuario(self):
        self.__controlador_usuarios.abre_tela()
        
    def encerra_sistema(self):
        exit(0)
        
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario, 0: self.encerra_sistema}
        
        while True:
            lista_opcoes[self.__tela_sistema.menu_opcoes()]()
            #opcao_escolhida = self.__tela_sistema.menu_opcoes
            #funcao_escolhida = lista_opcoes[opcao_escolhida]
            #funcao_escolhida()
