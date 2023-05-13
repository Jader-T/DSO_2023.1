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
        print("2 - Menu lojas")
        print("3 - Menu produtos")
        print("4 - Menu cotações") #mudar para cotações
        print("5 - Menu compras")
        print("0 - Encerrar Sistema")
        while True:
            try:
                opcao = int(input('Escolha a opção: ').strip())
                if opcao not in [0, 1, 2, 3, 4, 5, 0]:
                    print('Opção inválida, por favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")