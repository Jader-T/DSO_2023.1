

class TelaLoja:
    def __init__(self, controlador):
        self.__controlador = controlador

    @staticmethod
    def mostra_opcoes_loja(self):
        print('='*10, 'Menu Lojas', '='*10)
        print('1: Adicionar loja')
        print('2: Listar lojas')
        print('0: Retornar para a tela inicial')
        print('10: Retornar para o menu de produtos')
        while True:
            try:
                opcao = int(input('Opção: ').strip())
                if opcao not in [0, 1, 2, 10]:
                    print('Opção inválida, favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    @staticmethod
    def pega_dados_loja(self):
        print('='*10, 'Dados Loja', '='*10)
        try:

            nome = input('Digite o nome da loja: ').strip()
            site = input('Coloque aqui o link da loja: ').strip()
            if not nome or not site:
                raise ValueError("Nome e site da loja são obrigatórios.")
            return {"nome": nome, "site": site}
        except KeyboardInterrupt:
            print("Você interrompeu a execução do programa!")

    @staticmethod
    def mostra_loja(dados_loja):
        print("#"*20)
        print("Nome da loja: ", dados_loja["nome"])
        print("Site da loja: ", dados_loja["site"])
        print("#"*20)

    def pega_nome_loja(self):
        print('-'*10, "Selecionando a loja", '-'*10)
        return input("Informe o nome da loja: ")

    def mostra_msg(self, msg):
        print(msg)