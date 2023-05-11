from datetime import datetime

class TelaCompra:
    def __init__(self, controlador):
        self.__controlador = controlador

    @staticmethod
    def mostra_opcoes_compra(self):
        print('=' * 10, 'Menu Compras', '=' * 10)
        print('1: Comprar')
        print('2: Listar Compras')
        print('3: Gerar relatorio')
        print('0: Retornar')
        try:
            opcao = int(input('Opção: ').strip())
            #verificar se a opção é valida
            assert opcao in [0, 1, 2, 3]
            return opcao
        except ValueError:
            print("O valor digitado é inválido, favor digitar um número inteiro")
        except AssertionError:
            print("Opção inválida, digite uma opção válida")
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

    @staticmethod
    def pega_dados_compra(self):
        '''Verificar se esse tratamento de exceções está correto'''

        print("=" * 10, "Dados Compra", "=" * 10)
        while True:
            cotacao = input('Digite aqui o código da cotacao: ').strip()
            transportadora = input('Digite o nome da transportadora: ').strip()
            data_inserida = input('Digite a data de compra no formato DD/MM/AAAA: ').strip()
            try:
                data = datetime.strptime(data_inserida, '%d/%m/%Y')
                return {"data": data, "cotacao": cotacao, "transportadora": transportadora}
            except ValueError:
                print("A data inserida é inválida. Tente novamente.")

    @staticmethod
    def mostra_compra(dados_compra):
        print("Data da compra:: ", dados_compra["data"])
        print("Cotacao: ", dados_compra["cotacao"])
        print("Transportadora: ", dados_compra["transportadora"])
        print("\n")

    def mostra_msg(self, msg):
        print(msg)