import PySimpleGUI as sg


class TelaLoja:
    def __init__(self, controlador):
        self.__controlador = controlador

    @staticmethod
    def mostra_opcoes_loja(self):
        layout = [
            [sg.Text(text="Menu Lojas", font=('Arial', 16, 'bold'))],
            [sg.Text(text='Escolha a opção:', font=('Arial', 14))],
            [sg.Button(button_text="Adicionar loja", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Listar lojas", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Adicionar endereço de uma filial", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Listar endereço das filiais", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Retornar", font=('Arial', 14, 'bold'))],
        ]
        window = sg.Window("Cadastro de Lojas", layout, element_justification="center",
                           size=(350, 400), font=('Arial', 14, 'bold'))

        mapeamento_eventos = {
            "Adicionar loja": 1,
            "Listar lojas": 2,
            "Adicionar endereço de uma filial": 3,
            "Listar endereço das filiais": 4,
            "Retornar": 0}
        while True:
            event, values = window.read()
            if event in mapeamento_eventos:
                opcao = mapeamento_eventos[event]
                window.close()
                return opcao

    @staticmethod
    def pega_dados_loja(self):
        try:
            layout = [
                [sg.Text(text="Dados da Loja", font=('Arial', 12))],
                [sg.Text(text="Nome:  ", font=('Arial', 14, 'bold')), sg.InputText(key="nome", size=(15, 1))],
                [sg.Text(text="Site:  ", font=('Arial', 14, 'bold')), sg.InputText(key="site", size=(15, 1))],
                [sg.Text('')],
                [sg.Button(button_text="Confirmar")],
            ]
            window = sg.Window("Dados da Loja:", layout, element_justification="left", size=(350, 400))
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "Confirmar":
                    nome = values["nome"]
                    site = values["site"]
                    window.close()
                    return {"nome": nome, "site": site}
            window.close()
            return None
        except Exception as e:
            print("Erro ao obter dados da loja", e)
            return None

    @staticmethod
    def mostra_loja(dados_loja):
        try:
            for lojas in dados_loja:
                layout = [
                    [sg.Text(f"Nome: {lojas['nome']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Site: {lojas['site']}", font=('Arial', 14, 'bold'))],
                    [sg.Button("Proximo", font=('Arial', 14, 'bold'))],
                ]
                window = sg.Window('Informações da Loja ', layout, size=(350, 400), element_justification='left')

                while True:
                    event, _ = window.read()
                    if event == sg.WINDOW_CLOSED or event == "Proximo":
                        break
                window.close()
        except Exception as e:
            print('Erro ao exibir dados da loja', repr(e))

    def pega_nome_loja(self):
        try:
            layout = [
                [sg.Text("Nome da loja que deseja selecionar:", font=('Arial', 12, 'bold'))],
                [sg.Input(key='nome', size=(20, 1))],
                [sg.Button("Selecionar", size=(15, 1), font=('Arial', 14, 'bold'))],
                [sg.Text('')],
            ]
            window = sg.Window("Selecionar uma loja", layout, element_justification='center')

            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    nome = None
                    break

                elif event == "Selecionar":
                    nome = values["nome"]
                    break
            window.close()

            if not nome:
                raise ValueError("\nO nome da loja não pode estar vazio.\n")
            return nome
        except ValueError as ve:
            print(f"Erro ao selecionar loja: {ve}")
        except Exception as e:
            print(f"Erro ao selecionar loja: {e}")

    def mostra_msg(self, msg):
        sg.Popup(msg, font=('Arial', 14, 'bold'))

    def pega_dados_endereco(self):
        try:
            layout = [
                [sg.Text(text="Dados do endereço", font=('Arial', 12))],
                [sg.Text(text="Pais:  ", font=('Arial', 14, 'bold')), sg.InputText(key="pais", size=(15, 1))],
                [sg.Text(text="Estado:  ", font=('Arial', 14, 'bold')), sg.InputText(key="estado", size=(15, 1))],
                [sg.Text('')],
                [sg.Button(button_text="Confirmar")],
            ]
            window = sg.Window("Dados do endereço", layout, element_justification="left", size=(350, 400))
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "Confirmar":
                    pais = values["pais"]
                    estado = values["estado"]
                    window.close()
                    return {"pais": pais, "estado": estado}
            window.close()
            return None
        except Exception as e:
            print("Erro ao obter dados do endereço", e)
            return None

    @staticmethod
    def mostra_enderecos(dados_endereco):
        try:
            for endereco in dados_endereco:
                layout = [
                    [sg.Text(text="Endereços da loja selecionada", font=('Arial', 16))],
                    [sg.Text(f"Pais: {endereco['pais']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Estado: {endereco['estado']}", font=('Arial', 14, 'bold'))],
                    [sg.Button("Proximo", font=('Arial', 14, 'bold'))],
                ]
                window = sg.Window('Dados dos endereços', layout, size=(350, 400), element_justification='left')

                while True:
                    event, _ = window.read()
                    if event == sg.WINDOW_CLOSED or event == "Proximo":
                        break
                window.close()
        except Exception as e:
            print('Erro ao exibir dados dos endereços', repr(e))
            