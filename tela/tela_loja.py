

class TelaLoja:
    def __init__(self, controlador):
        self.__controlador = controlador

    @staticmethod
    def mostra_opcoes_loja(self):
        print('='*10, 'Menu Lojas', '='*10)
        print('1: Adicionar loja')
        print('2: Alterar loja')
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
    def mostra_loja(self, dados_loja):
        print("Nome da loja: ", dados_loja["nome"])
        print("Site da loja: ", dados_loja["site"])
        print("\n")