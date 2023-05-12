import time
from tela.tela_usuario import TelaUsuario
from modelo.pessoa_fisica import PessoaFisica
from modelo.pessoa_juridica import PessoaJuridica


class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__telaUsuarios = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
    
    def inclui_usuario(self):
        dados_usuario = self.__telaUsuarios.pega_dados_usuario()
        if "cpf" in dados_usuario: #se pessoa fisica utiliza a classe PessoaFisica
            nome  = dados_usuario["nome"]
            fone  = dados_usuario["fone"]
            email = dados_usuario["email"]
            cpf   = dados_usuario["cpf"]
            senha = dados_usuario["senha"]
            usuario = PessoaFisica(nome, fone, email, cpf, senha) 

        elif "cnpj" in dados_usuario: #se pessoa juridica utiliza a classe PessoaJuridica
            nome  = dados_usuario["nome"]
            fone  = dados_usuario["fone"]
            email = dados_usuario["email"]
            cnpj  = dados_usuario["cnpj"]
            senha = dados_usuario["senha"]
            usuario = PessoaJuridica(nome, fone, email, cnpj, senha)
        else:
            self.__telaUsuarios.mostra_mensagem("Tipo de usuário inválido!")
            return
        
        self.__usuarios.append(usuario)
        self.__telaUsuarios.mostra_mensagem("Usuário adicionado com sucesso!\n Redirecionando-o para o menu principal...")
        time.sleep(2)
        self.__controlador_sistema.inicializa_sistema()

    def altera_usuario(self):
        self.lista_usuarios()
        nome_usuario = self.__telaUsuarios.selecionar_usuario()
        usuario = self.busca_usuario_por_nome(nome_usuario)

        if (usuario is not None) and "cpf" in self.__telaUsuarios.pega_dados_usuario():
            novos_dados_usuario = self.__telaUsuarios.pega_dados_usuario()
            self.__telaUsuarios.mostra_mensagem("Digite os novos dados do usuário desejado")
            usuario.nome  = novos_dados_usuario["nome"]
            usuario.fone  = novos_dados_usuario["fone"]
            usuario.email = novos_dados_usuario["email"]
            usuario.cpf   = novos_dados_usuario["cpf"]
            usuario.senha = novos_dados_usuario["senha"]
            self.__telaUsuarios.mostra_mensagem("")
            self.__telaUsuarios.mostra_mensagem("Usuário alterado com sucesso!")
            self.__telaUsuarios.mostra_mensagem("")
            self.lista_usuarios()
        #implementar aqui o tryexcept
            #self.__telaUsuarios.mostra_mensagem("Usuário não Existe") 
        
        else:
            if (usuario is not None) and "cnpj" in self.__telaUsuarios.pega_dados_usuario():
                novos_dados_usuario = self.__telaUsuarios.pega_dados_usuario()
                self.__telaUsuarios.mostra_mensagem("Digite os novos dados do usuário desejado")
                usuario.nome  = novos_dados_usuario["nome"]
                usuario.fone  = novos_dados_usuario["fone"]
                usuario.email = novos_dados_usuario["email"]
                usuario.cnpj  = novos_dados_usuario["cnpj"]
                usuario.senha = novos_dados_usuario["senha"]
                self.__telaUsuarios.mostra_mensagem("")
                self.__telaUsuarios.mostra_mensagem("Usuário alterado com sucesso!")
                self.__telaUsuarios.mostra_mensagem("")            
                self.lista_usuarios()
            #implementar aqui o tryexcept    
                #self.__telaUsuarios.mostra_mensagem("Usuário não Existe")
                
    def exclui_usuario(self):
        self.lista_usuarios()
        nome_usuario = self.__telaUsuarios.selecionar_usuario()
        usuario = self.busca_usuario_por_nome(nome_usuario)
        if(usuario is not None):
            self.__usuarios.remove(usuario)
            self.__telaUsuarios.mostra_mensagem("")
            self.__telaUsuarios.mostra_mensagem("Usuário excluido com sucesso!")
            self.__telaUsuarios.mostra_mensagem("") 
            self.lista_usuarios()
        else:
            self.__telaUsuarios.mostra_mensagem("Usuário informado não existe")
            
    
    def lista_usuarios(self):
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()
        for usuario in self.__usuarios:
       
            if tipo_usuario == "Pessoa Física":
                for usuario in self.__usuarios:
                    self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "email": usuario.email, "cpf": usuario.cpf})
            elif tipo_usuario == "Pessoa Jurídica":
                for usuario in self.__usuarios:
                    self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "email": usuario.email, "cnpj": usuario.cnpj})#Ta dando BUG!!!
                
    def busca_usuario_por_nome(self, nome: str):
        for usuario in self.__usuarios:
            if isinstance(usuario, PessoaFisica) and usuario.nome == nome:
                return usuario
        return None

    def busca_usuario_por_nome_e_senha(self, nome: str, senha: str):
        for usuario in self.__usuarios:
            if (usuario.nome == nome and usuario.senha == senha):
                return usuario
        return None
    
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario, 2: self.altera_usuario, 3: self.exclui_usuario, 4: self.lista_usuarios, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__telaUsuarios.campos_da_tela()]()

