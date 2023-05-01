

class TelaLoja:
    def __init__(self, controlador):
        self.__controlador = controlador

    def mostra_opcoes_loja(self):
        print('#'*30)
        print('1: Adicionar loja')
        print('2: Alterar loja')
        opcao = int(input('opção: '))

    def pega_dados_loja(self):
        nome = input('Digite o nome da loja: ')
        site = input('Coloque aqui o link da loja: ')
        return [nome, site]




