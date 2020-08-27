def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('ERRO: Por favor, digite um valor valido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompiada pelo usuário')
            return 0
        else:
            return n
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError,TypeError):
            print('ERRO: Por favor, digite um valor valido')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompiada pelo usuário')
            return 0
        else:
            return n
num = leiaInt('digite um valor:')
num2  = leiaFloat('Digite valor real:')
print(f'O numero digitado inteiro foi: {num}')
print(f'O numero digitado real foi: {num2}')