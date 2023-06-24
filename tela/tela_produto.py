import PySimpleGUI as sg

class TelaProduto:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_produto(self):
        layout = [
            [sg.Text(text="Menu produtos", font=('Arial', 16, 'bold'))],
            [sg.Text(text='Escolha a opção:', font=('Arial', 14))],
            [sg.Button(button_text="Adicionar produto", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Listar produtos", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Alterar produto", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Retornar", font=('Arial', 14, 'bold'))],
        ]
        window = sg.Window("Cadastro de produtos", layout, element_justification="center",
                           size=(350, 400), font=('Arial', 14, 'bold'))

        mapeamento_eventos = {
            "Adicionar produto": 1,
            "Listar produtos": 2,
            "Alterar produto": 3,
            "Retornar": 0}
        while True:
            event, values = window.read()
            if event in mapeamento_eventos:
                opcao = mapeamento_eventos[event]
                window.close()
                return opcao

    def pega_dados_produto(self):
        try:
            layout = [
                [sg.Text(text="Dados do produto", font=('Arial', 12))],
                [sg.Text(text="Nome:  ", font=('Arial', 14, 'bold')), sg.InputText(key="nome", size=(15, 1))],
                [sg.Text(text="Tipo:  ", font=('Arial', 14, 'bold')), sg.InputText(key="tipo", size=(15, 1))],
                [sg.Text('')],
                [sg.Button(button_text="Confirmar")],
            ]
            window = sg.Window("Dados do prouto", layout, element_justification="left", size=(350, 400))
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "Confirmar":
                    nome = values["nome"]
                    tipo = values["tipo"]
                    window.close()
                    return {"nome": nome, "tipo": tipo}
            window.close()
            return None
        except Exception as e:
            print("Erro ao obter dados da loja", e)
            return None


    def pega_nome_produto(self):
        try:
            layout = [
                [sg.Text("Nome do produto que deseja selecionar:", font=('Arial', 12, 'bold'))],
                [sg.Input(key='nome', size=(20, 1))],
                [sg.Button("Selecionar", size=(15, 1), font=('Arial', 14, 'bold'))],
                [sg.Text('')],
            ]
            window = sg.Window("Selecionar um produto", layout, element_justification='center')

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
                raise ValueError("\nO nome do produto não pode estar vazio.\n")
            return nome
        except ValueError as ve:
            print(f"Erro ao selecionar produto: {ve}")
        except Exception as e:
            print(f"Erro ao selecionar produto: {e}")

    @staticmethod
    def mostra_produto(dados_produto):
        try:
            for produto in dados_produto:
                layout = [
                    [sg.Text(f"Nome: {produto['nome']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Tipo: {produto['tipo']}", font=('Arial', 14, 'bold'))],
                    [sg.Button("Proximo", font=('Arial', 14, 'bold'))],
                ]
                window = sg.Window('Informações do Produto ', layout, size=(350, 400), element_justification='left')

                while True:
                    event, _ = window.read()
                    if event == sg.WINDOW_CLOSED or event == "Proximo":
                        break
                window.close()
        except Exception as e:
            print('Erro ao exibir dados do produto', repr(e))


    def mostra_msg(self, msg):
        sg.Popup(msg, font=('Arial', 14, 'bold'))
