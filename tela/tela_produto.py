

class TelaProduto:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_produto(self):
        print('='*10, 'Menu Produtos', '='*10)
        print('1: Adicionar produto')
        print('2: Listar produtos')
        print('0: Retornar')
        while True:
            try:
                opcao = int(input('Opção: ').strip())
                if opcao not in [0,1,2,]:
                    print('Opção inválida, favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")
    def pega_dados_produto(self):
        print('=' * 10, 'Dados Produto', '=' * 10)
        try:
            nome = input('Digite o nome do produto: ').strip()
            tipo = input('Digite a categoria do produto: ').strip()
            if not nome or not tipo:
                raise ValueError("Nome e site da loja são obrigatórios.")
            return {"nome": nome, "tipo": tipo}
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

    def pega_nome_produto(self):
        print("Selecionando o produto")
        return input("Informe o nome do produto: ")

    @staticmethod
    def mostra_produto(dados_produto):
        print("Nome do produto: ", dados_produto["nome"])
        print("Loja relacionada: ", dados_produto["loja"])
        print("Categoria do produto: ", dados_produto["tipo"])
        print("\n")

    def mostra_msg(self, msg):
        print(msg)