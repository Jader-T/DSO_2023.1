import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        sg.ChangeLookAndFeel('DarkBlue')

    def tela_opcao_inicial(self):
        layout = [
            [sg.Text("Shop Tracer", font=("Arial", 20, "bold"))],
            [sg.Text("", size=(30, 1))],
            [sg.Button(button_text="Fazer login", font=("Arial", 14, "bold"), size=(15, 1))],
            [sg.Button(button_text="Cadastrar usuário", font=("Arial", 14, "bold"), size=(15, 1))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("", size=(30, 1))],
            [sg.Cancel(font=("Arial", 14, "bold"), size=(15, 1))]
        ]
        window = sg.Window("Shop Tracer", layout, element_justification='center',
                           finalize=True, size=(300, 400))

        while True:
            event, values = window.read()
            if event == "Fazer login":
                opcao = 1
                break
            elif event == "Cadastrar usuário":
                opcao = 2
                break
            elif event == sg.WINDOW_CLOSED or event == 'Cancel':
                opcao = None
                break

        window.close()
        return opcao

    def menu_opcoes(self):
        layout = [
            [sg.Text("Shop Tracer", font=("Arial", 20, "bold"))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Escolha a opção desejada:")],
            [sg.Button(button_text="Menu de usuários", size=(15, 1), font=("Arial", 14, 'bold'))],
            [sg.Button(button_text="Menu de lojas", size=(15, 1), font=("Arial", 14, 'bold'))],
            [sg.Button(button_text="Menu de produtos", size=(15, 1), font=("Arial", 14, 'bold'))],
            [sg.Button(button_text="Menu de cotações", size=(15, 1), font=("Arial", 14, 'bold'))],
            [sg.Button(button_text="Menu de compras", size=(15, 1), font=("Arial", 14, 'bold'))],
            [sg.Text("", size=(30, 1))],
            [sg.Button(button_text="Encerrar Sistema", size=(15, 1), font=('Arial', 14, 'bold'))],
        ]
        window = sg.Window("Shop Tracer", layout, element_justification='c'
                           , finalize=True, size=(350, 400))

        while True:
            event, _ = window.read()
            if event == "Menu de usuários":
                opcao = 1
                break
            elif event == "Menu de lojas":
                opcao = 2
                break
            elif event == "Menu de produtos":
                opcao = 3
                break
            elif event == "Menu de cotações":
                opcao = 4
                break
            elif event == "Menu de compras":
                opcao = 5
                break
            elif event == "Encerrar Sistema" or event == sg.WINDOW_CLOSED:
                opcao = 0
                break
        window.close()
        return opcao

    def tela_login(self):
        layout = [
            [sg.Text("          Shop Tracer", font=("Arial", 20, "bold"))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Digite seu usuário:", font=("Arial", 14)),
             sg.Input(key="usuario", size=(15, 1))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Digite sua senha:  ", font=("Arial", 14)),
             sg.Input(key="senha", password_char="*", size=(15, 1))],
            [sg.Text("", size=(30, 1))],
            [sg.Button("Confirmar", size=(15, 1))]
        ]
        window = sg.Window("Shop Tracer", layout, element_justification='left',
                           finalize=True, size=(350, 400))

        while True:
            event, values = window.read()
            if event == "Confirmar":
                nome = values["usuario"].strip()
                senha = values["senha"].strip()
                if nome != "" and senha != "":
                    break
                sg.popup("Nome de usuário e senha não podem ser vazios!")

            elif event == sg.WINDOW_CLOSED:
                nome = None
                senha = None
                break

        window.close()
        return {"usuario": nome, "senha": senha}

    def mensagem(self, msg):
        sg.popup(msg, auto_close=True, font=('Arial', 14, 'bold'))
