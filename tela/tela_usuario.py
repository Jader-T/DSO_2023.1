import PySimpleGUI as sg


class TelaUsuario:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkBlue')

    def campos_da_tela(self):
        layout = [
            [sg.Text(text="Configurações de Usuário", font=('Arial', 16, 'bold'))],
            [sg.Text(text='Escolha a opção:', font=('Arial', 14))],
            [sg.Button(button_text="Incluir usuário", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Alterar usuário", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Excluir usuário", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Listar usuários", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Voltar", font=('Arial', 14, 'bold'))],
        ]
        window = sg.Window("Cadastro de Usuários", layout, element_justification="center",
                           size=(350, 400), font=('Arial', 14, 'bold'))

        while True:
            event, values = window.read()
            if event == "Incluir usuário":
                opcao = 1
                break
            elif event == "Alterar usuário":
                opcao = 2
                break
            elif event == "Excluir usuário":
                opcao = 3
                break
            elif event == "Listar usuários":
                opcao = 4
                break
            elif event == "Voltar":
                opcao = 0
                break
        window.close()
        return opcao

    def seleciona_tipo_usuario(self):
        tipo_user = ""
        layout = [
            [sg.Text("Selecione o Tipo de Usuário:", font=('Arial', 14))],
            [sg.Button(button_text="Pessoa Física", size=(15, 1), font=('Arial', 14))],
            [sg.Button(button_text="Pessoa Jurídica", size=(15, 1), font=('Arial', 14))],
        ]

        window = sg.Window("Seleção de Tipo de Usuário", layout, finalize=True,
                           element_justification="Center", size=(350, 400))

        while True:
            event, _ = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Pessoa Física":
                tipo_user = "Pessoa Física"
                break
            elif event == "Pessoa Jurídica":
                tipo_user = "Pessoa Jurídica"
                break

        window.close()
        return tipo_user

    def pega_dados_usuario(self):
        try:
            tipo_usuario = self.seleciona_tipo_usuario()
            if tipo_usuario == "Pessoa Física":
                layout = [
                    [sg.Text(text="Tipo de usuário selecionado: Pessoa Física", font=('Arial', 12))],
                    [sg.Text(text="Nome:  ", font=('Arial', 14, 'bold')), sg.InputText(key="Nome", size=(15, 1))],
                    [sg.Text(text="Fone:  ", font=('Arial', 14, 'bold')), sg.InputText(key="Fone", size=(15, 1))],
                    [sg.Text(text="Email: ", font=('Arial', 14, 'bold')), sg.InputText(key="Email", size=(15, 1))],
                    [sg.Text(text="Senha:", font=('Arial', 14, 'bold')), sg.InputText(key="Senha", size=(15, 1))],
                    [sg.Text(text="CPF:   ", font=('Arial', 14, 'bold')), sg.InputText(key="cpf", size=(15, 1))],
                    [sg.Text('')],
                    [sg.Button(button_text="Confirmar")],
                ]
            elif tipo_usuario == "Pessoa Jurídica":
                layout = [
                    [sg.Text(text="Tipo de usuário selecionado: Pessoa Jurídica", font=('Arial', 12))],
                    [sg.Text(text="Nome: ", font=('Arial', 14, 'bold')), sg.InputText(key="Nome", size=(15, 1))],
                    [sg.Text(text="Fone: ", font=('Arial', 14, 'bold')), sg.InputText(key="Fone", size=(15, 1))],
                    [sg.Text(text="Email:", font=('Arial', 14, 'bold')), sg.InputText(key="Email", size=(15, 1))],
                    [sg.Text(text="Senha:", font=('Arial', 14, 'bold')), sg.InputText(key="Senha", size=(15, 1))],
                    [sg.Text(text="CNPJ: ", font=('Arial', 14, 'bold')), sg.InputText(key="cnpj", size=(15, 1))],
                    [sg.Text('')],
                    [sg.Button(button_text="Confirmar")],
                ]
            else:
                layout = [
                    [sg.Text("Opção inválida selecionada")],
                ]
                return None

            window = sg.Window("Dados do Usuário", layout, element_justification="left", size=(350, 400))

            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "Confirmar":
                    if tipo_usuario == "Pessoa Física":
                        nome = values["Nome"]
                        fone = values["Fone"]
                        email = values["Email"]
                        senha = values["Senha"]
                        cpf = values["cpf"]
                        window.close()
                        return {"nome": nome, "fone": fone, "email": email, "cpf": cpf, "senha": senha}
                    elif tipo_usuario == "Pessoa Jurídica":
                        nome = values["Nome"]
                        fone = values["Fone"]
                        email = values["Email"]
                        senha = values["Senha"]
                        cnpj = values["cnpj"]
                        window.close()
                        return {"nome": nome, "fone": fone, "email": email, "cnpj": cnpj, "senha": senha}

            window.close()
            return None
        except Exception as e:
            print("Erro ao obter dados do usuário", e)
            return None

    def mostra_usuario(self, dados_usuario):
        try:
            tipo_usuario = ""
            if "cpf" in dados_usuario:
                tipo_usuario = "Pessoa Física"
                layout = [
                    [sg.Text(f"Tipo de usuário: {tipo_usuario}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Nome {dados_usuario['nome']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Email {dados_usuario['email']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Cpf {dados_usuario['cpf']}", font=('Arial', 14,'bold'))],
                    [sg.Button("Fechar", font=('Arial', 14, 'bold'))],
                ]

            else:
                tipo_usuario = "Pessoa Jurídica"
                layout = [
                    [sg.Text(f"Tipo de usuário: {tipo_usuario}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Nome {dados_usuario['nome']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Email {dados_usuario['email']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Cnpj {dados_usuario['cnpj']}", font=('Arial', 14, 'bold'))],
                    [sg.Button("Fechar", font=('Arial', 14, 'bold'))],
                ]

            window = sg.Window('Informações do Usuário ', layout, size=(350, 400), element_justification='left')

            while True:
                event, _ = window.read()

                if event == sg.WINDOW_CLOSED or event == "Fechar":
                    break

            window.close()

        except Exception as e:
            print('Erro ao exibir dados do usuário', repr(e))

    def mostra_mensagem(self, msg):
        sg.Popup(msg, font=('Arial', 14, 'bold'))

    def selecionar_usuario(self):
        try:
            layout = [
                [sg.Text("Nome do usuário que deseja selecionar:", font=('Arial', 12, 'bold'))],
                [sg.Input(key='Nome', size=(20, 1))],
                [sg.Button("Selecionar", size=(15, 1), font=('Arial', 14, 'bold'))],
                [sg.Text('')],
            ]

            window = sg.Window("Selecione um usuário", layout, element_justification='center')

            while True:
                event, values = window.read()

                if event == sg.WINDOW_CLOSED:
                    nome = None
                    break

                elif event == "Selecionar":
                    nome = values["Nome"]
                    break

            window.close()

            if not nome:
                raise ValueError("\nO nome do usuário não pode estar vazio.\n")
            return nome
        except ValueError as ve:
            print(f"Erro ao selecionar usuário: {ve}")
        except Exception as e:
            print(f"Erro ao selecionar usuário: {e}")
