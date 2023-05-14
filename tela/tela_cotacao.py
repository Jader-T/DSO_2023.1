

class TelaCotacao:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_cotacao(self):
        print('=' * 10, 'Menu Cotação', '=' * 10)
        print('1: Adicionar cotação')
        print('2: Listar cotações')
        print('3: Remover cotação')
        print('4: Gerar relatório')
        print('0: Retornar para o menu inicial\n')
        while True:
            try:
                opcao = int(input('Opção: ').strip())
                if opcao not in [0, 1, 2, 3, 4]:
                    print('Opção inválida, por favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    def pega_dados_cotacao(self):
        print('=' * 10, 'Dados Cotação', '=' * 10)
        while True:
            try:
                valor = input('Digite o preço: ').strip()
                preco = float(valor)
                if not preco:
                    raise ValueError
                return {"preco": preco}
            except ValueError:
                print("Valor inválido, por favor digite um valor em reais")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    @staticmethod
    def mostra_cotacao(dados_cotacao):
        print("#" * 30)
        print("Preço da cotação: ", "R$", dados_cotacao["preco"])
        print("Nome do produto: ", dados_cotacao["nome_produto"])
        print("Loja relacionada: ", dados_cotacao["loja"])
        print("Código da cotação: ", dados_cotacao["codigo"])
        print("#" * 30)

    def pega_codigo_cotacao(self):
        print('-'*10, "Selecionando a cotação", '-'*10)
        while True:
            try:
                codigo = input("Informe o codigo da cotacao: ").strip()
                return codigo
            except ValueError:
                print("Valor inválido, favor fornecer um número inteiro")
            break
    
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
        print("="*10,"Relatório de Cotações","="*10)
        print("Preço da cotação: ", "R$", dados_cotacao["preco"])
        print("Nome do produto: ", dados_cotacao["nome_produto"])
        print("Loja relacionada: ", dados_cotacao["loja"])
        print("Código da cotação: ", dados_cotacao["codigo"])
        print("=" * 42)
                
    

    def mostra_msg(self, msg):
        print(msg)

    def pega_nome_cotacao(self):
        print('-'*10, "Selecionando a cotação", '-'*10)
        while True:
            try:
                produto_cotacao = input("Informe o nome do produto da cotação: ").strip()
                return produto_cotacao
            except KeyboardInterrupt:
                print("Você parou a execução do programa")
            break