from view.telaUsuario import TelaUsuario
from model.usuario import Usuario


class ControladorUsuários(Usuario):
    def __init__(self):
        self.__usuarios = []
        self.__telaUsuarios = TelaUsuario()
        
            
        
    def inclui_usuario(self):
        dados_usuario = self.__telaUsuarios.pega_dados_usuario()
        usuario = Usuario(dados_usuario["nome"], dados_usuario['fone'], dados_usuario['email'])#depois ver a questão do cpf e cnpj
        
    def altera_usuario(self):
        self.lista_usuarios()
        nome_usuario = self.__telaUsuarios.selecionar_usuario()
        usuario = self.busca_usuario_por_cpf(nome_usuario)
    
    def exclui_usuario(self):
        pass    
    
    def lista_usuarios(self):
        for usuario in self.__usuarios:
            self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "telefone": usuario.telefone, "email": usuario.email})
            
    def busca_usuario_por_cpf_ou_cnpj(self, cpf: str, cnpj: str):#ver como tratar a escolha de cpf e cnpj
        pass