

class TelaCotacao:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_cotacao(self):
        print('=' * 10, 'Menu Cotação', '=' * 10)
        print('1: Adicionar cotação')
        print('2: Listar cotações')
        print('3: Alterar cotação')
        print('4: Gerar relatório')
        print('0: Retornar para a tela inicial')
        print('10: Ir para o menu Compras')
        while True:
            while True:
                try:
                    opcao = int(input('Opção: ').strip())
                    if opcao not in [0, 1, 2, 10]:
                        print('Opção inválida, por favor digite novamente!')
                    else:
                        return opcao
                except ValueError:
                    print("O valor digitado é inválido, favor digitar um número inteiro!")
                except KeyboardInterrupt:
                    print("Você interrompeu a execução do programa!")

    def pega_dados_cotacao(self):
        print('=' * 10, 'Dados Cotação', '=' * 10)
        try:
            preco = input('Digite o preço: ').strip()
            #produto = input('Escolha o produto: ').strip()
            if not preco:
                raise ValueError("Nome e site da loja são obrigatórios.")
            return {"preco": preco}
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

    @staticmethod
    def mostra_cotacao(dados_cotacao):
        print("#" * 20)
        print("Preço da cotação: ", "R$", dados_cotacao["preco"])
        print("Nome do produto: ", dados_cotacao["nome_produto"])
        print("Loja relacionada: ", dados_cotacao["loja"])
        print("Código da cotação: ", dados_cotacao["codigo"])
        print("#" * 20)

    def pega_codigo_cotacao(self):
        print('-'*10, "Selecionando a cotação", '-'*10)
        return input("Informe o codigo da cotacao: ")

    def mostra_msg(self, msg):
        print(msg)