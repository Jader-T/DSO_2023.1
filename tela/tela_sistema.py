class TelaSistema():

    def tela_opcao_inicial(self):
        while True:
            try:
                print("="*10, "Shop Tracer", "="*10)
                print("")
                print("Escolha a opção: ")
                print("1 - Fazer login")
                print("2 - Cadastrar usuário")
                print("")
                opcao = int(input("Escolha a opção: "))
                return opcao
            except ValueError:
                print("Opção inválida! Digite um número inteiro.\n")

    def menu_opcoes(self):
        print("="*10, "Shop Tracer", "="*10)
        print("")
        print("Escolha a opcao desejada: ")
        print("")
        print("1 - Menu usuários")
        print("2 - Menu lojas")
        print("3 - Menu produtos")
        print("4 - Menu cotações")
        print("5 - Menu compras")
        print("0 - Encerrar Sistema")
        print("")
        while True:
            try:
                opcao = int(input("Escolha a opção: ")).strip())
                if opcao not in [0, 1, 2, 3, 4, 5]:
                    print('Opção inválida, por favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    def tela_login(self):
        print("="*10, "Shop Tracer", "="*10)
        while True:
            nome = input("Digite seu usuário: ")
            if nome.strip() == "":
                print("Nome de usuário vazio! Tente novamente.\n")
            else:
                break
        while True:
            senha = input("Digite sua senha: ")
            if senha.strip() == "":
                print("Senha vazia! Tente novamente.\n")
            else:
                break
        return {"usuario": nome, "senha": senha}

    def mensagem(self, msg):
        print(msg)
