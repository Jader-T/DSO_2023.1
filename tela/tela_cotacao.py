import PySimpleGUI as sg


class TelaCotacao:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_cotacao(self):
        layout = [
            [sg.Text(text="Menu Cotação", font=('Arial', 16, 'bold'))],
            [sg.Text(text='Escolha a opção:', font=('Arial', 14))],
            [sg.Button(button_text="Adicionar cotação", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Listar cotação", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Remover cotação", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Gerar relatório", font=('Arial', 14, 'bold'))],
            [sg.Button(button_text="Retornar", font=('Arial', 14, 'bold'))],
        ]
        window = sg.Window("Cadastro de cotações", layout, element_justification="center",
                           size=(350, 400), font=('Arial', 14, 'bold'))

        mapeamento_eventos = {
            "Adicionar cotação": 1,
            "Listar cotação": 2,
            "Remover cotação": 3,
            "Gerar relatório": 4,
            "Retornar": 0}
        while True:
            event, values = window.read()
            if event in mapeamento_eventos:
                opcao = mapeamento_eventos[event]
                window.close()
                return opcao

    def pega_dados_cotacao(self):
        try:
            layout = [
                [sg.Text(text="Dados da cotação", font=('Arial', 12))],
                [sg.Text(text="Preço:  ", font=('Arial', 14, 'bold')), sg.InputText(key="preco", size=(15, 1))],
                [sg.Text('')],
                [sg.Button(button_text="Confirmar")],
            ]
            window = sg.Window("Dados da cotação", layout, element_justification="left", size=(350, 400))
            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    break
                elif event == "Confirmar":
                    valor = values["preco"]
                    preco = float(valor)
                    window.close()
                    return {"preco": preco}
            window.close()
            return None
        except Exception as e:
            print("Erro ao obter dados da cotação", e)
            return None

    @staticmethod
    def mostra_cotacao(dados_cotacao):
        try:
            for cotacao in dados_cotacao:
                layout = [
                    [sg.Text(f"Preço: {cotacao['preco']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Produto: {cotacao['nome_produto']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Loja: {cotacao['loja']}", font=('Arial', 14, 'bold'))],
                    [sg.Text(f"Código da cotação: {cotacao['codigo']}", font=('Arial', 14, 'bold'))],
                    [sg.Button("Proximo", font=('Arial', 14, 'bold'))],
                ]
                window = sg.Window('Informações da Loja ', layout, size=(350, 400), element_justification='left')

                while True:
                    event, _ = window.read()
                    if event == sg.WINDOW_CLOSED or event == "Proximo":
                        break
                window.close()
        except Exception as e:
            print('Erro ao exibir dados da cotacao', repr(e))

    def pega_codigo_cotacao(self):
        try:
            layout = [
                [sg.Text("Código da cotação:", font=('Arial', 12, 'bold'))],
                [sg.Input(key='codigo', size=(20, 1))],
                [sg.Button("Selecionar", size=(15, 1), font=('Arial', 14, 'bold'))],
                [sg.Text('')],
            ]
            window = sg.Window("Selecionar uma cotação", layout, element_justification='center')

            while True:
                event, values = window.read()
                if event == sg.WINDOW_CLOSED:
                    codigo = None
                    break

                elif event == "Selecionar":
                    codigo = values["codigo"]
                    break
            window.close()

            if not codigo:
                raise ValueError("\nO codigo da cotação não pode estar vazio.\n")
            return codigo
        except ValueError as ve:
            print(f"Erro ao selecionar cotação: {ve}")
        except Exception as e:
            print(f"Erro ao selecionar cotação: {e}")

# -------------------- relatorio ----------------------------------#

    def pega_valor_inicial(self):
        while True:
            layout = [
                [sg.Text("Geração de relatório", font=("Arial", 16, "bold"))],
                [sg.Text('Valor minimo', font=('Arial', 14, 'bold')), sg.Input("Digite o valor mínimo: ", key='valor_minimo')],
                [sg.Button("Selecionar", font=('Arial', 14, 'bold'))],

            ]
            window = sg.Window("Geração de relatório", layout, size=(300, 400))

            while True:
                event, values = window.read()

                if event == sg.WINDOW_CLOSED:
                    valor_inicial = None
                    break
                elif event == "Selecionar":
                    valor_inicial = values["valor_minimo"]
                    break

            window.close()

            if not valor_inicial:
                raise ValueError("O valor inicial não pode estar vazio.")
            return valor_inicial

    def pega_valor_final(self):
        while True:
            layout = [
                [sg.Text("Filtros do relatório", font=("Arial", 16, "bold"))],
                [sg.Text('Valor maximo:', font=('Arial', 14, 'bold')), sg.Input("Digite o valor máximo: ", key='valor_maximo')],
                [sg.Button("Selecionar", font=('Arial', 14, 'bold'))],
            ]
            window = sg.Window("Geração de relatório", layout, size=(300, 400))

            while True:
                event, values = window.read()

                if event == sg.WINDOW_CLOSED:
                    valor_final = None
                    break
                elif event == "Selecionar":
                    valor_final = values["valor_maximo"]
                    break

            window.close()

            if not valor_final:
                raise ValueError("O valor inicial não pode estar vazio.")
            return valor_final

    def pega_produto(self):
        while True:
            layout = [
                [sg.Text("Filtros do relatório", font=("Arial", 16, "bold"))],
                [sg.Text('Produto:', font=('Aria', 14, 'bold')), sg.Input("Digite o produto: ", key='produto')],
                [sg.Button("Selecionar", font=('Arial', 14, 'bold'))],

            ]
            window = sg.Window("Dados para o relatório", layout, size=(300, 400))

            while True:
                event, values = window.read()

                if event == sg.WINDOW_CLOSED:
                    produto = None
                    break
                elif event == "Selecionar":
                    produto = values["produto"]
                    break

            window.close()

            if not produto:
                raise ValueError("O valor inicial não pode estar vazio.")
            return produto

    @staticmethod
    def mostra_relatorio(dados_cotacao):
        layout = [
            [sg.Text(text=("=" * 10, "Relatório de Cotações", "=" * 10))],
        ]

        for cotacao in dados_cotacao:
            layout.append([sg.Text(f"Preço da cotação: {cotacao['preco']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Nome do produto: {cotacao['nome_produto']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Loja relacionada: {cotacao['loja']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text(f"Código da cotação: {cotacao['codigo']}", font=('Arial', 14, 'bold'))])
            layout.append([sg.Text("-" * 90)])

        layout.append([sg.Button("Fechar", font=('Arial', 14, 'bold'))])

        window = sg.Window("Relatório de cotação", layout)

        event, _ = window.read()

        window.close()

    # ---------------------------------------------------------------------------#

    def mostra_msg(self, msg):
        sg.Popup(msg, font=('Arial', 14, 'bold'))

    def pega_nome_cotacao(self):
        try:
            layout = [
                [sg.Text("Nome do produto da cotação:", font=('Arial', 12, 'bold'))],
                [sg.Input(key='nome', size=(20, 1))],
                [sg.Button("Selecionar", size=(15, 1), font=('Arial', 14, 'bold'))],
                [sg.Text('')],
            ]
            window = sg.Window("Selecionar uma cotação", layout, element_justification='center')

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
                raise ValueError("\nO codigo da cotação não pode estar vazio.\n")
            return nome
        except ValueError as ve:
            print(f"Erro ao selecionar cotação: {ve}")
        except Exception as e:
            print(f"Erro ao selecionar cotação: {e}")
