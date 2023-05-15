import time
from tela.tela_usuario      import TelaUsuario
from modelo.pessoa_fisica   import PessoaFisica
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
            self.__telaUsuarios.mostra_mensagem("\nTipo de usuário inválido!\n")
            return
        self.__usuarios.append(usuario)
        self.__telaUsuarios.mostra_mensagem("\nUsuário adicionado com sucesso!\n")
        time.sleep(2)
        #if origem == "inicializa_sistema":
        self.__controlador_sistema.inicializa_sistema()
        #else:
            #self.abre_tela(origem)

    def altera_usuario(self):
        self.lista_usuarios()
        nome_usuario = self.__telaUsuarios.selecionar_usuario()
        usuario = self.busca_usuario_por_nome(nome_usuario)
        novos_dados_usuario = self.__telaUsuarios.pega_dados_usuario()

        if usuario is None:
            self.__telaUsuarios.mostra_mensagem("\nUsuário não encontrado!\n")
            return

        if "cpf" in novos_dados_usuario:
            if not isinstance(usuario, PessoaFisica):
                self.__telaUsuarios.mostra_mensagem("\nNão é possível alterar o tipo do usuário!")
                return
            usuario.nome = novos_dados_usuario["nome"]
            usuario.fone = novos_dados_usuario["fone"]
            usuario.email = novos_dados_usuario["email"]
            usuario.cpf = novos_dados_usuario["cpf"]
            usuario.senha = novos_dados_usuario["senha"]
        elif "cnpj" in novos_dados_usuario:
            if not isinstance(usuario, PessoaJuridica):
                self.__telaUsuarios.mostra_mensagem("Não é possível alterar o tipo do usuário!")
                return
            usuario.nome = novos_dados_usuario["nome"]
            usuario.fone = novos_dados_usuario["fone"]
            usuario.email = novos_dados_usuario["email"]
            usuario.cnpj = novos_dados_usuario["cnpj"]
            usuario.senha = novos_dados_usuario["senha"]
        else:
            self.__telaUsuarios.mostra_mensagem("Tipo de usuário inválido!")
            return

        self.__telaUsuarios.mostra_mensagem("\nUsuário alterado com sucesso!\n")
        self.lista_usuarios()
                
    def exclui_usuario(self):
        self.lista_usuarios()
        nome_usuario = self.__telaUsuarios.selecionar_usuario()
        usuario = self.busca_usuario_por_nome(nome_usuario)
        if(usuario is not None):
            self.__usuarios.remove(usuario)
            self.__telaUsuarios.mostra_mensagem("\nUsuário excluido com sucesso!\n")
        else:
            self.__telaUsuarios.mostra_mensagem("Usuário informado não existe")
            
    
    def lista_usuarios(self):
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()
        for usuario in self.__usuarios:
            if isinstance(usuario, PessoaFisica) and tipo_usuario == "Pessoa Física":
                self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "email": usuario.email, "cpf": usuario.cpf})
            elif isinstance(usuario, PessoaJuridica) and tipo_usuario == "Pessoa Jurídica":
                self.__telaUsuarios.mostra_usuario({"nome": usuario.nome, "email": usuario.email, "cnpj": usuario.cnpj})
        else:
            pass

                
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

