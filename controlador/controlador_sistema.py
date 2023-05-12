from tela.tela_sistema import TelaSistema
from controlador.controlador_usuario import ControladorUsuarios
import time


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
            if self.faz_login(): # se ok, abre a tela inicial
                self.__tela_sistema.mensagem("Login realizado com sucesso!")
                self.abre_tela()
        else:
            if opcao == 2: #opcao 2 é cadastro
                self.__tela_sistema.mensagem("Você será direcionado para o cadastro de usuários")
                time.sleep(2)
                self.controlador_usuarios.inclui_usuario()  #abre o método de incluir usuario

    def faz_login(self):
        usuario_senha = self.__tela_sistema.tela_login()
        if self.controlador_usuarios.busca_usuario_por_nome_e_senha(usuario_senha["usuario"], usuario_senha["senha"]): #compara o usuario e senha do tela login com o busca por nome e senha
            return True
        else:      #se não houver usuário volta para a tela de login
            self.__tela_sistema.mensagem("")
            self.__tela_sistema.mensagem("Usuário não encontrado!\n Você será redirecionado a tela de login inicial...")
            time.sleep(1)
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
