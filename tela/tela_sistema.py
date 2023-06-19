import PySimpleGUI as sg


class TelaSistema:
    def __init__(self):
        sg.ChangeLookAndFeel('Black')
    def tela_opcao_inicial(self):
        layout = [
            [sg.Text("Shop Tracer", font=("Helvetica", 20))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Escolha a opção:", font=("Helvetica", 14))],
            [sg.Button("Fazer login")],
            [sg.Button("Cadastrar usuário")],
            [sg.Text("", size=(30, 1))],
        ]
        window = sg.Window("Shop Tracer", layout, element_justification='center', font=("arial", 14), finalize=True, size=(300, 250))

        while True:
            event, _ = window.read()
            if event == "Fazer login":
                opcao = 1
                break
            elif event == "Cadastrar usuário":
                opcao = 2
                break
            elif event == sg.WINDOW_CLOSED:
                opcao = None
                break

        window.close()
        return opcao

    def menu_opcoes(self):
        layout = [
            [sg.Text("Shop Tracer", font=("Helvetica", 20))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Escolha a opção desejada:", font=("Helvetica", 14))],
            [sg.Button("1 - Menu usuários")],
            [sg.Button("2 - Menu lojas")],
            [sg.Button("3 - Menu produtos")],
            [sg.Button("4 - Menu cotações")],
            [sg.Button("5 - Menu compras")],
            [sg.Text("", size=(30, 1))],
            [sg.Button("0 - Encerrar Sistema")],
        ]
        window = sg.Window("Shop Tracer", layout, element_justification='c', font=("Helvetica", 14), finalize=True, size=(350, 400))

        while True:
            event, _ = window.read()
            if event == "1 - Menu usuários":
                opcao = 1
                break
            elif event == "2 - Menu lojas":
                opcao = 2
                break
            elif event == "3 - Menu produtos":
                opcao = 3
                break
            elif event == "4 - Menu cotações":
                opcao = 4
                break
            elif event == "5 - Menu compras":
                opcao = 5
                break
            elif event == "0 - Encerrar Sistema" or event == sg.WINDOW_CLOSED:
                opcao = 0
                break

        window.close()
        return opcao

    def tela_login(self):
        layout = [
            [sg.Text("Shop Tracer", font=("Helvetica", 20))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Digite seu usuário:", font=("Helvetica", 14))],
            [sg.Input(key="-USUARIO-", size=(30, 1), font=("Helvetica", 14))],
            [sg.Text("", size=(30, 1))],
            [sg.Text("Digite sua senha:", font=("Helvetica", 14))],
            [sg.Input(key="-SENHA-", password_char="*", size=(30, 1), font=("Helvetica", 14))],
            [sg.Text("", size=(30, 1))],
            [sg.Button("OK", font=("Helvetica", 14))]
        ]
        window = sg.Window("Shop Tracer", layout, element_justification='c', font=("Helvetica", 14), finalize=True, size=(350, 300))

        while True:
            event, values = window.read()
            if event == "OK":
                nome = values["-USUARIO-"].strip()
                senha = values["-SENHA-"].strip()
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
        sg.popup(msg)
