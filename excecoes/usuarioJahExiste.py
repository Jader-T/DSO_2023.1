class UsuarioJahExiste(Exception):
    def __init__(self):
        self.mensagem = "usuário informado ja existe"
        super().__init__(self.mensagem)
