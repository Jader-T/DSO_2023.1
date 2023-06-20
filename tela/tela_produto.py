

class TelaProduto:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_produto(self):
        print('='*10, 'Menu Produtos', '='*10)
        print('1: Adicionar produto')
        print('2: Listar produtos')
        print('3: Alterar produto')
        print('0: Retornar para o menu inicial\n')
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

    def pega_dados_produto(self):
        print('=' * 10, 'Dados Produto', '=' * 10)
        while True:
            try:
                nome = input('Digite o nome do produto: ').strip()
                tipo = input('Digite a categoria do produto: ').strip()
                if not nome or not tipo:
                    raise ValueError
                return {"nome": nome, "tipo": tipo}
            except ValueError:
                print("Nome e site da loja são obrigatórios.")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    def pega_nome_produto(self):
        print('-'*10, "Selecionando o produto", '-'*10)
        return input("Informe o nome do produto: ")

    @staticmethod
    def mostra_produto(dados_produto):
        print("#" * 30)
        print("Nome do produto: ", dados_produto["nome"])
        print("Categoria do produto: ", dados_produto["tipo"])
        print("#" * 30)

    def mostra_msg(self, msg):
        print(msg)
