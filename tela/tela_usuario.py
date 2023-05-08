class TelaUsuario():
    def campos_da_tela(self):
        print("_"*10, "Configurações de Usuários", "_"*10)
        print("Escolha a opção:")
        print("1 - Incluir Usuário")
        print("2 - Alterar Usuário")
        print("3 - Listar Usuários")
        print("4 - Excluir Usuário")
            
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
        tipo_usuario = self.seleciona_tipo_usuario()
        print("Tipo de usuário selecionado:", tipo_usuario)
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        
        if tipo_usuario == "Pessoa Física":
            cpf = input("CPF: ")
            return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf}
        else:
            cnpj = input("CNPJ: ")
            return {"nome": nome, "telefone": telefone, "email": email, "cnpj": cnpj}
    
    def mostra_usuario(self, dados_usuario):
        tipo_usuario = ""
        if "cpf" in dados_usuario:
            tipo_usuario = "Pessoa Física"
            print("Tipo de usuário: ", tipo_usuario)
            print("Nome: ", dados_usuario["nome"])
            print("Telefone: ", dados_usuario["telefone"])
            print("Email: ", dados_usuario["email"])
            print("CPF: ", dados_usuario["cpf"])
        else:
            tipo_usuario = "Pessoa Jurídica"
            print("Tipo de usuário: ", tipo_usuario)
            print("Nome: ", dados_usuario["nome"])
            print("Telefone: ", dados_usuario["telefone"])
            print("Email: ", dados_usuario["email"])
            print("CNPJ: ", dados_usuario["cnpj"])
    
    def mostra_mensagem(self, msg):
        print(msg)
        
    def selecionar_usuario(self):
        nome = input("Nome do Usuário que deseja selecionar: ") #definir depois se vai buscar pelo nome ou cpf/cnpj
        return nome