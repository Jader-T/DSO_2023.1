

class TelaUsuario:
    def campos_da_tela(self):
        print("="*10, "Configurações de Usuários", "="*10)
        print("Escolha a opção:")
        print("1 - Incluir Usuário")
        print("2 - Alterar Usuário")
        print("3 - Excluir Usuário")
        print("4 - Listar Usuários")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if opcao not in range(5):
                    print("Opção inválida. Digite um número entre 0 e 4.")
                else:
                    return opcao
            except ValueError:
                print("Opção inválida. Digite um número inteiro entre 0 e 4.")

    def seleciona_tipo_usuario(self):
        try:
            opcoes = ["Pessoa Física", "Pessoa Jurídica"]
            mensagem = "Selecione o tipo de usuário: "
            return self.__mostra_menu(opcoes, mensagem)
        except Exception as e:
            print("Erro ao selecionar tipo de usuário:", e)

    def __mostra_menu(self, opcoes, mensagem):
        try:
            print(mensagem)
            for i, opcao in enumerate(opcoes):
                print(f"{i+1} - {opcao}")
            escolha = int(input("Escolha uma opção: "))
            return opcoes[escolha-1]
        except ValueError:
            print("Valor digitado não é um número inteiro.")
            return None
        except IndexError:
            print("Opção selecionada não existe.")
            return None
        except TypeError:
            print("Selecione uma das duas opções!")
            return None

    def pega_dados_usuario(self):
        try:
            tipo_usuario = self.seleciona_tipo_usuario()
            if tipo_usuario == "Pessoa Física":
                print("Tipo de usuário selecionado: Pessoa Física")
                nome = input("Nome: ")
                fone = int(input("Telefone: "))
                email = input("Email: ")
                senha = input("Senha: ")
                cpf = input("Cpf: ")
                return {"nome": nome, "fone": fone, "email": email, "cpf": cpf, "senha": senha}
            elif tipo_usuario == "Pessoa Jurídica":
                print("Tipo de usuário selecionado: Pessoa Jurídica")
                nome = input("Nome: ")
                fone = int(input("Telefone: "))
                email = input("Email: ")
                senha = input("Senha: ")
                cnpj = input("Cnpj: ")
                return {"nome": nome, "fone": fone, "email": email, "cnpj": cnpj, "senha": senha}
            else:
                print("Opção inválida selecionada.")
                return None
        except ValueError:
            print("Erro ao obter dados do usuário: telefone deve ser um número inteiro.")
            return None
        except Exception as e:
            print("Erro ao obter dados do usuário:", e)
            return None

    def mostra_usuario(self, dados_usuario):
        try:
            tipo_usuario = ""
            if "cpf" in dados_usuario:
                tipo_usuario = "Pessoa Física"
                print("Tipo de usuário: ", tipo_usuario)
                print("Nome: ", dados_usuario["nome"])
                print("Email: ", dados_usuario["email"])
                print("Cpf: ", dados_usuario["cpf"])
                print("\n")
            else:
                tipo_usuario = "Pessoa Jurídica"
                print("Tipo de usuário: ", tipo_usuario)
                print("Nome: ", dados_usuario["nome"])
                print("Email: ", dados_usuario["email"])
                print("Cnpj: ", dados_usuario["cnpj"])
                print("\n")
        except:
            print("Erro ao exibir dados do usuário")
    
    def mostra_mensagem(self, msg):
        try:
            print(msg)
        except:
            print("Erro ao exibir mensagem")
        
    def selecionar_usuario(self):
        try:
            nome = input("Nome do Usuário que deseja selecionar: ")
            if not nome:
                raise ValueError("O nome do usuário não pode estar vazio.")
            return nome
        except ValueError as ve:
            print(f"Erro ao selecionar usuário: {ve}")
        except Exception as e:
            print(f"Erro ao selecionar usuário: {e}")
