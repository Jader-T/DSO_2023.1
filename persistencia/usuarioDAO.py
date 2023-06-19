from persistencia import DAO
from modelo.usuario import Usuario


class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('usuarios.pkl')

    def add(self, usuario: Usuario):
        if (isinstance(usuario.nome, int)) and (usuario is not None) \
                and isinstance(usuario, Usuario):
            super().add(usuario.nome, usuario)

    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
