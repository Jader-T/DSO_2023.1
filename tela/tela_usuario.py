class TelaUsuario():
    def campos_da_tela(self):
        try:
            print("_"*10, "Configurações de Usuários", "_"*10)
            print("Escolha a opção:")
            print("1 - Incluir Usuário")
            print("2 - Alterar Usuário")
            print("3 - Listar Usuários")
            print("4 - Excluir Usuário")
            print("0 - Retornar")
        except:
            print("Erro ao exibir tela de configurações de usuários")
            
    def seleciona_tipo_usuario(self):
        try:
            opcoes = ["Pessoa Física", "Pessoa Jurídica"]
            mensagem = "Selecione o tipo de usuário: "
            return self.__mostra_menu(opcoes, mensagem)
        except:
            print("Erro ao selecionar tipo de usuário")
    
    def __mostra_menu(self, opcoes, mensagem):
        try:
            print(mensagem)
            for i, opcao in enumerate(opcoes):
                print(f"{i+1} - {opcao}")
            escolha = int(input("Escolha uma opção: "))
            return opcoes[escolha-1]
        except (ValueError, IndexError):
            print("Opção inválida selecionada")
               
    def pega_dados_usuario(self):
        
        if self.seleciona_tipo_usuario() == "Pessoa Física": 
            print("Tipo de usuário selecionado: Pessoa Física")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            senha = input("Senha: ")
            cpf = input("Cpf: ")
            return {"nome": nome, "telefone": telefone, "email": email, "cpf": cpf, "senha": senha}
        else:
            print("Tipo de usuário selecionado: Pessoa Jurídica")
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            senha = input("Senha: ")
            cnpj = input("Cnpj: ")
            return {"nome": nome, "telefone": telefone, "email": email, "cnpj": cnpj, "senha": senha}
    
    def mostra_usuario(self, dados_usuario):
        try:
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
        except:
            print("Erro ao exibir dados do usuário")
    
    def mostra_mensagem(self, msg):
        try:
            print(msg)
        except:
            print("Erro ao exibir mensagem")
        
    def selecionar_usuario(self):
        try:
            nome = input("Nome do Usuário que deseja selecionar: ") #definir depois se vai buscar pelo nome ou cpf/cnpj
            return nome
        except:
            print("Erro ao selecionar usuário")        
