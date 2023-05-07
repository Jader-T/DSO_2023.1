from tela.telaUsuario import TelaUsuario
from modelo.usuario import Usuario
from modelo.pessoaFisica import PessoaFisica
from modelo.PessoaJuridica import PessoaJuridica


class ControladorUsuários:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__telaUsuarios = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
        
    def inclui_usuario(self):
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario() # pergunta se é pessoa física ou jurídica
        dados_usuario = self.__telaUsuarios.pega_dados_usuario()
        
        if tipo_usuario == "Pessoa Física":
            cpf = dados_usuario["cpf"]
            nome = dados_usuario["nome"]
            telefone = dados_usuario["fone"]
            email = dados_usuario["email"]
            usuario = PessoaFisica(cpf, nome, telefone, email)
        elif tipo_usuario == "Pessoa Jurídica":
            cnpj = dados_usuario["cnpj"]
            razao_social = dados_usuario["razao_social"]
            telefone = dados_usuario["fone"]
            email = dados_usuario["email"]
            usuario = PessoaJuridica(cnpj, razao_social, telefone, email)
        else:
            self.__telaUsuarios.mostra_mensagem("Tipo de usuário inválido!")
            return
            
        self.__usuarios.append(usuario)
        self.__telaUsuarios.mostra_mensagem("Usuário adicionado com sucesso!")

        
    def altera_usuario(self):
        self.lista_usuarios()
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()
        
        if tipo_usuario == "Pessoa Física":
            cpf_usuario = self.__telaUsuarios.selecionar_usuario()
            usuario = self.busca_usuario_por_cpf(cpf_usuario)
                
            if (usuario is not None):
                novos_dados_usuario = self.__telaUsuarios.pega_dados_usuario()
                usuario.nome = novos_dados_usuario["Nome"]
                usuario.fone = novos_dados_usuario["Fone"]
                usuario.email = novos_dados_usuario["Email"]
                usuario.cpf = novos_dados_usuario["Cpf"]
                self.lista_usuarios()
            else:
                self.__telaUsuarios.mostra_mensagem("Usuário não Existe") 
                    
        elif tipo_usuario == "Pessoa Jurídica":
            cnpj_usuario = self.__telaUsuarios.selecionar_usuario()
            usuario = self.busca_usuario_por_cnpj(cnpj_usuario)
            if (usuario is not None):
                novos_dados_usuario = self.__telaUsuarios.pega_dados_usuario()
                usuario.nome = novos_dados_usuario["Nome"]
                usuario.fone = novos_dados_usuario["Fone"]
                usuario.email = novos_dados_usuario["Email"]
                usuario.cnpj = novos_dados_usuario["Cnpj"]
                self.lista_usuarios()
            else:
                self.__telaUsuarios.mostra_mensagem("Usuário não Existe")
                
    def exclui_usuario(self):
        pass    
    
    def lista_usuarios(self):
        for usuario in self.__usuarios:
            self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "telefone": usuario.telefone, "email": usuario.email})
            
    def busca_usuario_por_cpf_ou_cnpj(self, cpf: str, cnpj: str):#ver como tratar a escolha de cpf e cnpj
        pass
    
    def retornar(self):
        #self.__controlador_sistema.abre_tela()
        pass
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__telaUsuarios.campos_da_tela()]()