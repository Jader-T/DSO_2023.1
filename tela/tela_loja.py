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
        window = sg.Window("Cadastro de Usuários", layout, element_justification="center",
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
            window = sg.Window("Dados do Usuário", layout, element_justification="left", size=(350, 400))
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
        print("#" * 30)
        print("Nome da loja: ", dados_loja["nome"])
        print("Site da loja: ", dados_loja["site"])
        print("#" * 30)

    def pega_nome_loja(self):
        print('-'*10, "Selecionando a loja", '-'*10)
        return input("Informe o nome da loja: ")

    def mostra_msg(self, msg):
        print(msg)

    def pega_dados_endereco(self):
        print('-' * 10, "Informe a localidade da filial", '-' * 10)
        while True:
            try:
                pais = input('Digite o país: ')
                estado = input('Digite o estado: ')
                if not pais or not estado:
                    raise ValueError
                return {"pais": pais, "estado": estado}
            except ValueError:
                print("Pais e estado são obrigatórios.")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    @staticmethod
    def mostra_enderecos(dados_endereco):
        print("#" * 30)
        print("Endereços da loja selecionada:\n")
        print("Pais: ", dados_endereco["pais"])
        print("Estado: ", dados_endereco["estado"])
        print("#" * 30)