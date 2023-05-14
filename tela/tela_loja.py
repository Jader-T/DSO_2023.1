

class TelaLoja:
    def __init__(self, controlador):
        self.__controlador = controlador

    @staticmethod
    def mostra_opcoes_loja(self):
        print('='*10, 'Menu Lojas', '='*10)
        print('1: Adicionar loja')
        print('2: Listar lojas')
        print('3: Adicionar endereço')
        print('0: Retornar para o menu inicial\n')
        while True:
            try:
                opcao = int(input('Opção: ').strip())
                if opcao not in [0, 1, 2, 3, 10]:
                    print('Opção inválida, por favor digite novamente!')
                else:
                    return opcao
            except ValueError:
                print("O valor digitado é inválido, favor digitar um número inteiro!")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    @staticmethod
    def pega_dados_loja(self):
        print('='*10, 'Dados Loja', '='*10)
        while True:
            try:
                nome = input('Digite o nome da loja: ').strip()
                site = input('Coloque aqui o link da loja: ').strip()
                if not nome or not site:
                    raise ValueError
                return {"nome": nome, "site": site}
            except ValueError:
                print("Nome e site da loja são obrigatórios.")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")

    @staticmethod
    def mostra_loja(dados_loja):
        print("#" * 30)
        print("Nome da loja: ", dados_loja["nome"])
        print("Site da loja: ", dados_loja["site"])
        print("#" * 30)

    def pega_nome_loja(self):
        print('-'*10, "Selecionando a loja", '-'*10)
        return input("Informe o nome da loja: ")

    def mostra_msg(self, msg):
        print(msg)

    def pega_dados_endereco(self):
        print('-' * 10, "Informe a localidade da filial", '-' * 10)
        while True:
            try:
                pais = input('Digite o país: ')
                estado = input('Digite o estado: ')
                if not pais or not estado:
                    raise ValueError
                return {"pais": pais, "estado": estado}
            except ValueError:
                print("Pais e estado são obrigatórios.")
            except KeyboardInterrupt:
                print("Você interrompeu a execução do programa!")