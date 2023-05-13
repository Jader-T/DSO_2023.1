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
        while True:
            try:
                print("="*10, "Shop Tracer", "="*10)
                print("")
                print("Escolha a opcao desejada: ")
                print("")
                print("1 - Configurar Usuários")
                print("0 - Encerrar Sistema")
                print("")
                opcao = int(input("Escolha a opção: "))
                if opcao not in [0, 1]:
                    raise ValueError("Opção inválida! Digite 0 ou 1.\n")
                return opcao
            except ValueError as ve:
                print(ve)
    
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
