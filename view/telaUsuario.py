class TelaUsuario():
    #depois ver o tratamento de dados
    def campos_da_tela(self):
        print("________ Configurações de Usuários ________")
        print("Escolha a opção:")
        #colocar todas as opcoes aqui
        
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
    
    
    def selecionar_usuario(self):
        nome = input("Nome do Usuário que deseja selecionar: ")
        return nome
    