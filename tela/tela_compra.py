from datetime import datetime
import PySimpleGUI as sg


class TelaCompra:
    def __init__(self, controlador):
        self.__controlador = controlador

    @staticmethod
    def mostra_opcoes_compra(self):
        layout = [
            [sg.Text(text="Menu de Compras", font=('Arial', 16, 'bold'))],
            [sg.Text(text='Escolha a opção:', font=('Arial', 14))],
            [sg.Button(button_text="Registrar compra", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Listar compras", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Gerar relatorio", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Retornar", font=('Arial', 14, 'bold'))],
        ]
        window = sg.Window("Registro de compras", layout, element_justification="center",
                           size=(350, 400), font=('Arial', 14, 'bold'))

        mapeamento_eventos = {
            "Registrar compra": 1,
            "Listar compras": 2,
            "Gerar relatorio": 3,
            "Retornar": 0}
        while True:
            event, values = window.read()
            if event in mapeamento_eventos:
                opcao = mapeamento_eventos[event]
                window.close()
                return opcao

    @staticmethod
    def pega_dados_compra(self):
        try:
            layout = [
                [sg.Text(text="Dados da compra", font=('Arial', 12))],
                [sg.Text(text="Data da compra:  ", font=('Arial', 14, 'bold')), sg.InputText(key="data", size=(15, 1))],
                [sg.Text(text="Transportadora:  ", font=('Arial', 14, 'bold')), sg.InputText(key="transportadora", size=(15, 1))],
                [sg.Text('')],
                [sg.Button(button_text="Confirmar")],
            ]
            window = sg.Window("Dados da Loja:", layout, element_justification="left", size=(350, 400))
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "Confirmar":
                    data = values["data"]
                    transportadora = values["transportadora"]
                    window.close()
                    return {"data": data, "transportadora": transportadora}
            window.close()
            return None
        except Exception as e:
            print("Erro ao obter dados da loja", e)
            return None

    @staticmethod
    def mostra_compra(dados_compra):
        try:
            for compra in dados_compra:
                layout = [
                    [sg.Text(f"Data da compra: {compra['data']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Código da cotação: {compra['dados_codigo']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Produto comprado: {compra['dados_produto']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Preço: {compra['dados_preco']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Loja: {compra['dados_loja']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Transportadora: {compra['transportadora']}", font=('Arial', 14, 'bold'))],
                    [sg.Button("Proximo", font=('Arial', 14, 'bold'))],
                ]
                window = sg.Window('Informações da compra ', layout, size=(350, 400), element_justification='left')

                while True:
                    event, _ = window.read()
                    if event == sg.WINDOW_CLOSED or event == "Proximo":
                        break
                window.close()
        except Exception as e:
            print('Erro ao exibir dados da loja', repr(e))

    def pega_data_inicial(self):
        layout = [
            [sg.Text("Digite a data inicial no formato dd/mm/aaaa: ")],
            [sg.Input(key='data_inicial')],
            [sg.Button('Confirmar')]
        ]

        window = sg.Window('Filtros do relatório', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Confirmar':
                data_texto = values['data_inicial']
                try:
                    data = datetime.strptime(data_texto, '%d/%m/%Y')
                    window.close()
                    return data
                except ValueError:
                    sg.Popup('Data invalida. Digite novamente.')

    def pega_data_final(self):
        layout = [
            [sg.Text("Digite a data final no formato dd/mm/aaaa: ")],
            [sg.Input(key='data_final')],
            [sg.Button('Confirmar')]
        ]

        window = sg.Window('Filtros do relatório', layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Confirmar':
                data_texto = values['data_final']
                try:
                    data = datetime.strptime(data_texto, '%d/%m/%Y')
                    window.close()
                    return data
                except ValueError:
                    sg.Popup('Data invalida. Digite novamente.')

    @staticmethod
    def mostra_relatorio(dados_compra):
        layout = [
            [sg.Text(text="Relatório de Compras", justification="center", font=('Arial', 16, 'bold'))],
        ]

        for compra in dados_compra:
            layout.append([sg.Text(f"Data da compra: {compra['data']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Código da cotação: {compra['dados_codigo']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Produto comprado: {compra['dados_produto']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Preço: {compra['dados_preco']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Transportadora: {compra['transportadora']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text("-" * 90)])

        layout.append([sg.Button("Fechar", font=('Arial', 14, 'bold'))])

        window = sg.Window("Relatório de Compras", layout)

        event, _ = window.read()

        window.close()

    def mostra_msg(self, msg):
        sg.Popup(msg, font=('Arial', 14, 'bold'))
