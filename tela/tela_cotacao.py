

class TelaCotacao:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_cotacao(self):
        print('=' * 10, 'Menu Cotação', '=' * 10)
        print('1: Adicionar cotação')
        print('2: Alterar cotação')
        print('3: Gerar relatório')
        print('0: Retornar')
        while True:
            try:
                opcao = int(input('Opção: ').strip())
                '''verificar se a opção é valida'''
                assert opcao in [0, 1, 2, 3]
                return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro")
            except AssertionError:
                print("Opção inválida, digite uma opção válida")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    def pega_dados_cotacao(self):
        print('=' * 10, 'Dados Cotação', '=' * 10)
        try:
            preco = input('Digite o preço: ').strip()
            produto = input('Escolha o produto: ').strip()
            if not preco or not produto:
                raise ValueError("Nome e site da loja são obrigatórios.")
            return {"preco": preco, "nome_produto": produto}
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

    @staticmethod
    def mostra_cotacao(self, dados_cotacao):
        print("Preço da cotação:: ", dados_cotacao["preco"])
        print("Nome do produto: ", dados_cotacao["nome_produto"])
        print("Código da cotação: ", dados_cotacao["codigo"])
        print("\n")

    def pega_codigo_cotacao(self):
        print("Selecionando a loja")
        return input("Informe o nome da loja: ")

    def mostra_msg(self, msg):
        print(msg)