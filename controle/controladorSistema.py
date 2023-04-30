from tela.telaSistema import TelaSistema
from controle.controladorUsuarios import ControladorUsuários

class ControladorSistema:
    def __init__(self):
        self.__controlador_usuarios = ControladorUsuários
        self.__tela_sistema = TelaSistema
    
    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios
    
    def inicializa_sistema(self):
        self.__abre_tela()
        
    def cadastra_usuario(self):
        self.__controlador_usuarios.abre_tela()
        
        