class TelaUsuario():
    #depois ver o tratamento de dados
    def campos_da_tela(self):
        print("________ Configurações de Usuários ________")
        print("Escolha a opção:")
        #colocar todas as opcoes aqui
    
    def seleciona_tipo_usuario(self):
        opcoes = ["Pessoa Física", "Pessoa Jurídica"]
        mensagem = "Selecione o tipo de usuário: "
        return self.__mostra_menu(opcoes, mensagem)
    
    def __mostra_menu(self, opcoes, mensagem):
        print(mensagem)
        for i, opcao in enumerate(opcoes):
            print(f"{i+1} - {opcao}")
        escolha = int(input("Escolha uma opção: "))
        return opcoes[escolha-1]    
        
    def pega_dados_usuario(self):        
        print("Pessoa Juridica?" )
        Tipo_de_Usuario = input(" 'S' ou 'N' ? ")
        if Tipo_de_Usuario == 'S':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cnpj = input("Cnpj: ")
        else:
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cpf = input("Cpf: ")
    
    def mostra_usuario(self, dados_usuario):
        pass
    
    def mostra_mensagem(self, msg):
        print(msg)
        
    def selecionar_usuario(self):
        nome = input("Nome do Usuário que deseja selecionar: ")
        return nome
    