from persistencia.DAO import DAO
from modelo.usuario import Usuario
from modelo.pessoa_fisica import PessoaFisica
from modelo.pessoa_juridica import PessoaJuridica


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if isinstance(usuario, PessoaFisica):
            super().add(usuario.cpf, usuario)
        elif isinstance(usuario, PessoaJuridica):
            super().add(usuario.cnpj, usuario)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key):
        # if isinstance(key):
        return super().remove(key)
