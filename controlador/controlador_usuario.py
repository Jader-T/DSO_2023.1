from tela.tela_usuario import TelaUsuario
from modelo.usuario import Usuario #ver se fato não vai ser nescessário usar depois
from modelo.pessoa_fisica import PessoaFisica
from modelo.pessoa_juridica import PessoaJuridica


class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__telaUsuarios = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
    #metodo para autenticação do usuário    
    #def autentica_usuario(self):
       # pass    
       
    def inclui_usuario(self):
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario() # pergunta se é pessoa física ou jurídica
        dados_usuario = self.__telaUsuarios.pega_dados_usuario()
        
        if tipo_usuario == "Pessoa Física": #se pessoa fisica
            cpf = dados_usuario["cpf"]
            nome = dados_usuario["nome"]
            telefone = dados_usuario["fone"]
            email = dados_usuario["email"]
            usuario = PessoaFisica(cpf, nome, telefone, email)
        elif tipo_usuario == "Pessoa Jurídica": #se pessoa juridica
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
        self.lista_usuarios()
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()
        
        if tipo_usuario == "Pessoa Física":
            cpf_usuario = self.__telaUsuarios.selecionar_usuario()
            usuario = self.busca_usuario_por_cpf(cpf_usuario)
            if (usuario is not None):
                self.__usuarios.remove(usuario)
                self.__telaUsuarios.mostra_mensagem("Usuário excluído com sucesso!")
                self.lista_usuarios()
            else:
                self.__telaUsuarios.mostra_mensagem("Usuário não existe.")
                        
        elif tipo_usuario == "Pessoa Jurídica":
            cnpj_usuario = self.__telaUsuarios.selecionar_usuario()
            usuario = self.busca_usuario_por_cnpj(cnpj_usuario)
            if (usuario is not None):
                self.__usuarios.remove(usuario)
                self.__telaUsuarios.mostra_mensagem("Usuário excluído com sucesso!")
                self.lista_usuarios()
            else:
                self.__telaUsuarios.mostra_mensagem("Usuário não existe.")

    
    def lista_usuarios(self):
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()

        if tipo_usuario == "Pessoa Física":
            for usuario in self.__usuarios:
                self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "telefone": usuario.telefone, "email": usuario.email, "cpf": usuario.cpf})
        elif tipo_usuario == "Pessoa Jurídica":
            for usuario in self.__usuarios:
                self.__telaUsuarios.mostra_usuario({"razao_social": usuario.razao_social, "telefone": usuario.telefone, "email": usuario.email, "cnpj": usuario.cnpj})
            
    def busca_usuario_por_cpf_ou_cnpj(self, cpf: str, cnpj: str):
        for usuario in self.__usuarios:
            if isinstance(usuario, PessoaFisica) and usuario.cpf == cpf:
                return usuario
            elif isinstance(usuario, PessoaJuridica) and usuario.cnpj == cnpj:
                return usuario
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario, 2: self.altera_usuario, 3: self.exclui_usuario, 4: self.lista_usuarios, 0: self.retornar}
        
        continua = True
        while continua:
            lista_opcoes[self.__telaUsuarios.campos_da_tela()]()