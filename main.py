import requests


def inicio():
    while True:
        x = int(input('O que deseja consultar? \n'
                      'Buscar Endereço pelo CEP: Digite 1\n'
                      'Buscar CEP pelo endereço: Digite 2\n'
                      'Cancelar: Digite 3\n'))
        if x not in [1, 2, 3]:
            print('Digite um valor válido!')
            continue
        if x == 1:
            buscar_endereco()
            break
        if x == 2:
            buscar_cep()
            break
        if x == 3:
            break


def buscar_endereco():
    while True:
        cep = input('Informe o CEP que deseja consultar: ')
        if len(cep) < 8 or len(cep) >= 9:
            print('Informe um CEP válido!')
            continue
        else:
            try:
                requisicao_endereco = requests.get('https://viacep.com.br/ws/' + cep + '/json/')
                date = requisicao_endereco.json()
                print('\nSeguem os dados da sua consulta para o CEP: ' + date['cep'])
                print('Estado: ' + date['uf'])
                print('Cidade: ' + date['localidade'])
                print('Bairro: ' + date['bairro'])
                print('Rua: ' + date['logradouro'])
                print('Complemento: ' + date['complemento'])
                break
            except:
                print('Não foi possível consultar')
                break


def buscar_cep():
    while True:
        uf = input('Informe a UF que deseja consultar: ')
        if len(uf) != 2:
            print('Informe uma UF válida!')
            continue
        cidade = input('Informe a cidade que deseja consultar: ')
        rua = input('Informe a rua que deseja consultar: ')
        try:
            requisicao_endereco = requests.get('https://viacep.com.br/ws/' + uf + '/' + cidade + '/' + rua + '/json/')
            date = str(requisicao_endereco.json())
            date = date[10:19]
            print('De acordo com os dados informados, seu CEP pode ser o: ' + date)
            break
        except:
            print('Não foi possível consultar')
            break


inicio()
