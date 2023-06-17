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
        print('4: Buscar compra')
        print('0: Retornar para tela inicial')
        while True:
            try:
                opcao = int(input('Opção: ').strip())
                if opcao not in [0, 1, 2, 3]:
                    print('Opção inválida, favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    @staticmethod
    def pega_dados_compra(self):
        '''Necessário adicionar mais um tratamento de exceções, para as variaveis cotacao e transportadora'''

        print("=" * 10, "Dados Compra", "=" * 10)
        while True:
            transportadora = input('Digite o nome da transportadora: ').strip()
            data_inserida = input('Digite a data de compra no formato DD/MM/AAAA: ').strip()
            try:
                data = datetime.strptime(data_inserida, '%d/%m/%Y')
                return {"data": data, "transportadora": transportadora}
            except ValueError:
                print("A data inserida é inválida. Tente novamente.")
                
    def pega_data_inicial(self):
        while True:
            try:
                data_texto = input("Digite a data inicial no formato dd/mm/aaaa: ").strip()
                data = datetime.strptime(data_texto, '%d/%m/%Y')
                return data.strptime('%d/%m/%Y')
            except ValueError:
                print("Data Inválida. Digite novamente.")
                
    def pega_data_final(self):
        while True:
            try:
                data_texto = input("Digite a data final no formato dd/mm/aaaa: ")
                data = datetime.strptime(data_texto, '%d/%m/%Y')
                return data.strptime('%d/%m/%Y')
            except ValueError:
                print("Data inválida. Digite novamente.")
    
    @staticmethod
    def mostra_relatorio(dados_compra):
        print("="*15,"Relatório de Compras","="*15)
        for compra in dados_compra:
            print("Data da compra: ", compra["data"])
            print("Código da cotação: ", compra["dados_codigo"])
            print("Produto comprado: ", compra["dados_produto"])
            print("Preço: ", "R$", compra["dados_preco"])
            print("Transportadora: ", compra["transportadora"])
            print("-" * 52)
        print("="*52)
                    
    
    @staticmethod
    def mostra_compra(dados_compra):
        print("#" * 30)
        print("Data da compra: ", dados_compra["data"])
        print("Código da cotação: ", dados_compra["dados_codigo"])
        print("Produto comprado: ", dados_compra["dados_produto"])
        print("Preço: ", "R$", dados_compra["dados_preco"])
        print("Transportadora: ", dados_compra["transportadora"])
        print("#" * 30)

    def mostra_msg(self, msg):
        print(msg)