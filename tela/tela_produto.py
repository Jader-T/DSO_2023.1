

class TelaProduto:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_produto(self):
        print('='*10, 'Menu Produtos', '='*10)
        print('1: Adicionar produto')
        print('2: Alterar produto')
        print('3: Gerar relatório')
        print('0: Retornar')
        try:
            opcao = int(input('Opção: ').strip())
#           verificar se a opção é valida
            assert opcao in [0, 1, 2]
            return opcao
        except ValueError:
            print("O valor digitado é inválido, favor digitar um número inteiro")
        except AssertionError:
            print("Opção inválida, digite uma opção válida")
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

    def pega_dados_produto(self):
        print('=' * 10, 'Dados Produto', '=' * 10)
        try:
            nome = input('Digite o nome do produto: ').strip()

            tipo = input('Digite a categoria do produto: ').strip()
            if not nome or not loja or not tipo:
                raise ValueError("Nome e site da loja são obrigatórios.")
            return {"nome": nome, "tipo": tipo}
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

