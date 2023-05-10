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
        opcao = self.__tela_sistema.tela_opcao_inicial()
        if opcao == 1: #opcao 1 é login
            if self.faz_login():
                self.abre_tela()
        else:
            if opcao == 2: #opcao 2 é cadastro
                self.controlador_usuarios.inclui_usuario()

    def faz_login(self):
        usuario_senha = self.__tela_sistema.tela_login()
        if self.controlador_usuarios.busca_usuario_por_nome_e_senha(usuario_senha["usuario"], usuario_senha["senha"]):
            return True
        else:
            print("")
            print("Usuário não encontrado!")
            self.inicializa_sistema()
    
    def configura_usuarios(self):
        self.__controlador_usuarios.abre_tela()
        
    def encerra_sistema(self):
        exit(0)
        
    def abre_tela(self):
        lista_opcoes = {1: self.configura_usuarios, 0: self.encerra_sistema}
        
        while True:
            opcao_escolhida = self.__tela_sistema.menu_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()