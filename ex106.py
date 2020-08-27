def ajuda(pa):
    help(pa)


def titulo():
    print('-' * 50)
    print('Sua Funcionalidade explicada')
    print('-' * 50)


sair = ''
while True:
    sair = input('Função ou biblioteca:')
    if sair.upper() == 'FIM':
        break
    else:
        ajuda(sair)


print('FIM')
