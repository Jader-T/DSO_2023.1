
class TelaSistema():

    def tela_opcao_inicial(self):
        print("="*10, "Shop Tracer", "="*10)
        print("Escolha a opção: ")
        print("1 - Fazer login")
        print("2 - Cadastrar usuário")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def menu_opcoes(self):
        print("="*10, "Shop Tracer", "="*10)
        print("Escolha a opcao desejada: ")
        print("")
        print("1 - Configurar Usuários")
        print("0 - Encerrar Sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def tela_login(self):
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")
        return {"usuario": usuario, "senha": senha}