class TelaSistema:
    #tela de login para iniciar sessão no sistema
    def tela_login(self):
        print("_________Shop Tracer__________")
        Usuário = input("Insira seu usuário: ")
    
    #tela inicial de opções do sistema
    def menu_opcoes(self):
        print("_________Shop Tracer__________")
        print("Escolha a opcao desejada: ")
        print("1 - Usuários")
        print("0 - Encerrar Sistema")
        opcao = int(input("Escolha a opção: "))
        #fazer aqui o tratamento de excessões
        return opcao