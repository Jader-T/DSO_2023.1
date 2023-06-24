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

    def pega_valor_inicial(self):
        while True:
            try:
                valor = input("Digite o valor mínimo: ")
                preco = float(valor)
                return preco
            except ValueError:
                print("Valor inválido. Digite novamente")
            except TypeError:
                print("A informação digitada deve ser um valor numérico!")

    def pega_valor_final(self):
        while True:
            try:
                valor = input("Digite o valor máximo: ")
                preco = float(valor)
                return preco
            except ValueError:
                print("Valor inválido. Digite novamente")
            except TypeError:
                print("A informação digitada deve ser um valor numérico!")

    @staticmethod
    def mostra_relatorio(dados_cotacao):
        print("="*10, "Relatório de Cotações", "="*10)
        print("Preço da cotação: ", "R$", dados_cotacao["preco"])
        print("Nome do produto: ", dados_cotacao["nome_produto"])
        print("Loja relacionada: ", dados_cotacao["loja"])
        print("Código da cotação: ", dados_cotacao["codigo"])
        print("=" * 42)

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

        print('-'*10, "Selecionando a cotação", '-'*10)
        while True:
            try:
                produto_cotacao = input("Informe o nome do produto da cotação: ").strip()
                return produto_cotacao
            except KeyboardInterrupt:
                print("Você parou a execução do programa")
            break
