from datetime import datetime

def pega_dados_compra():
    '''Verificar se esse tratamento de exceções está correto'''

    print("=" * 10, "Dados Compra", "=" * 10)
    while True:
        codigo_cotacao = input('Digite aqui o código da cotacao: ').strip()
        transportadora = input('Digite o nome da transportadora: ').strip()
        data_inserida = input('Digite a data de compra no formato DD/MM/AAAA: ').strip()
        try:
            data = datetime.strptime(data_inserida, '%d/%m/%Y')
            return {"data": data, "codigo_cotacao": codigo_cotacao, "transportadora": transportadora}
        except ValueError:
            print("A data inserida é inválida. Tente novamente.")

pega_dados_compra()