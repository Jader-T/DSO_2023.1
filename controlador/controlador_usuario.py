from tela.tela_usuario import TelaUsuario
from modelo.pessoa_fisica import PessoaFisica
from modelo.pessoa_juridica import PessoaJuridica
from persistencia.usuarioDAO import UsuarioDAO
from excecoes.usuarioJahExiste import UsuarioJahExiste

class ControladorUsuarios:
    def __init__(self, controlador_sistema):
        self.__usuario_DAO = UsuarioDAO()
        self.__telaUsuarios = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    @property
    def usuarios(self):
        return self.__usuario_DAO.get_all()

    def inclui_usuario(self):
        dados_usuario = self.__telaUsuarios.pega_dados_usuario()
        if "cpf" in dados_usuario:  # se pessoa fisica utiliza a classe PessoaFisica
            nome = dados_usuario["nome"]
            fone = dados_usuario["fone"]
            email = dados_usuario["email"]
            cpf = dados_usuario["cpf"]
            senha = dados_usuario["senha"]
            usuario = PessoaFisica(nome, fone, email, cpf, senha)

        elif "cnpj" in dados_usuario:  # se pessoa juridica utiliza a classe PessoaJuridica
            nome = dados_usuario["nome"]
            fone = dados_usuario["fone"]
            email = dados_usuario["email"]
            cnpj = dados_usuario["cnpj"]
            senha = dados_usuario["senha"]
            usuario = PessoaJuridica(nome, fone, email, cnpj, senha)
        else:
            self.__telaUsuarios.mostra_mensagem("\nTipo de usuário inválido!\n")
            return False
        self.__usuario_DAO.add(usuario)
        self.__telaUsuarios.mostra_mensagem("\nUsuário adicionado com sucesso!\n")
        return True

    def altera_usuario(self):
        novos_dados_usuario = self.__telaUsuarios.pega_dados_usuario()
        if "cpf" in novos_dados_usuario:
            tipo_usuario = "Pessoa Física"
            self.lista_usuarios(tipo_usuario)
            cpf_usuario = self.__telaUsuarios.selecionar_usuario_por_cpf()
            usuario = self.busca_usuario_por_cpf(cpf_usuario)
            if usuario is None:
                self.__telaUsuarios.mostra_mensagem("Usuário não encontrado!")
                return
            if not isinstance(usuario, PessoaFisica):
                self.__telaUsuarios.mostra_mensagem("\nNão é possível alterar o tipo do usuário!")
                return
            usuario.nome = novos_dados_usuario["nome"]
            usuario.fone = novos_dados_usuario["fone"]
            usuario.email = novos_dados_usuario["email"]
            usuario.cpf = novos_dados_usuario["cpf"]
            usuario.senha = novos_dados_usuario["senha"]
        elif "cnpj" in novos_dados_usuario:
            tipo_usuario = "Pessoa Jurídica"
            self.lista_usuarios(tipo_usuario)
            cnpj_usuario = self.__telaUsuarios.selecionar_usuario_por_cnpj()
            usuario = self.busca_usuario_por_cnpj(cnpj_usuario)
            if usuario is None:
                self.__telaUsuarios.mostra_mensagem("Usuário não encontrado!")
                return
            if not isinstance(usuario, PessoaJuridica):
                self.__telaUsuarios.mostra_mensagem("\nNão é possível alterar o tipo do usuário!")
                return
            usuario.nome = novos_dados_usuario["nome"]
            usuario.fone = novos_dados_usuario["fone"]
            usuario.email = novos_dados_usuario["email"]
            usuario.cnpj = novos_dados_usuario["cnpj"]
            usuario.senha = novos_dados_usuario["senha"]
        else:
            self.__telaUsuarios.mostra_mensagem("Tipo de usuário inválido!")
            return
        self.__telaUsuarios.mostra_mensagem("Usuário alterado com sucesso!")

    def exclui_usuario(self):
        tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()
        self.lista_usuarios(tipo_usuario)

        if tipo_usuario == 'Pessoa Física':
            cpf_usuario = self.__telaUsuarios.selecionar_usuario_por_cpf()
            usuario = self.busca_usuario_por_cpf(cpf_usuario)
            if usuario is not None and isinstance(usuario, PessoaFisica):
                self.__usuario_DAO.remove(usuario.cpf)
                self.__telaUsuarios.mostra_mensagem("Usuário excluido com sucesso!")
            else:
                self.__telaUsuarios.mostra_mensagem("Usuário informado não existe")
        elif tipo_usuario == 'Pessoa Jurídica':
            cnpj_usuario = self.__telaUsuarios.selecionar_usuario_por_cnpj()
            usuario = self.busca_usuario_por_cnpj(cnpj_usuario)
            if usuario is not None and isinstance(usuario, PessoaJuridica):
                self.__usuario_DAO.remove(usuario.cnpj)
                self.__telaUsuarios.mostra_mensagem("Usuário excluido com sucesso!")
            else:
                self.__telaUsuarios.mostra_mensagem("Usuário informado não existe")

    def lista_usuarios(self, tipo_usuario=None):
        if tipo_usuario is None:
            tipo_usuario = self.__telaUsuarios.seleciona_tipo_usuario()

        usuarios_listados = []

        for usuario in self.__usuario_DAO.get_all():
            if isinstance(usuario, PessoaFisica) and tipo_usuario == "Pessoa Física":
                usuarios_listados.append({"nome": usuario.nome, "email": usuario.email, "cpf": usuario.cpf})
            elif isinstance(usuario, PessoaJuridica) and tipo_usuario == "Pessoa Jurídica":
                usuarios_listados.append({"nome": usuario.nome, "email": usuario.email, "cnpj": usuario.cnpj})
        if usuarios_listados:
            self.__telaUsuarios.mostra_usuario(usuarios_listados)
        else:
            self.__telaUsuarios.mostra_mensagem('Nenhum usuário encontrado')

    def busca_usuario_por_cpf(self, cpf: int):
        for usuario in self.__usuario_DAO.get_all():
            if isinstance(usuario, PessoaFisica) and usuario.cpf == cpf:
                return usuario
        return None

    def busca_usuario_por_cnpj(self, cnpj: int):
        for usuario in self.__usuario_DAO.get_all():
            if isinstance(usuario, PessoaJuridica) and usuario.cnpj == cnpj:
                return usuario
        return None

    def busca_usuario_por_nome_e_senha(self, nome: str, senha: str):
        for usuario in self.__usuario_DAO.get_all():
            if usuario.nome == nome and usuario.senha == senha:
                return usuario
        return None

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.inclui_usuario, 2: self.altera_usuario, 3: self.exclui_usuario, 4: self.lista_usuarios,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__telaUsuarios.campos_da_tela()]()
