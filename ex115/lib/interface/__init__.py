def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} -{item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua opção:')
    return opc


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um valor valido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompiada pelo usuário')
            return 0
        else:
            return n
