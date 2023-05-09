class TelaSistema:
    #tela de login para iniciar sessão no sistema
    def tela_login(self):
        print("="*10, "Shop Tracer", "="*10)
        print("Escolha a opção: ")
        print("1 - Fazer login")
        print("2 - Cadastrar usuário")
        opcao = int(input("Escolha a opção: "))
        return opcao
    
    #tela inicial de opções do sistema
    def menu_opcoes(self):
        print("="*10, "Shop Tracer", "="*10)
        print("Escolha a opcao desejada: ")
        print("")
        print("1 - Configurar Usuários")
        print("2 - Produtos")
        print("0 - Encerrar Sistema")
        opcao = int(input("Escolha a opção: "))
        return opcao