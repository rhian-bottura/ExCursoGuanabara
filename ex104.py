def i(inteiro):
    if inteiro.isnumeric():
        inteiro = int(inteiro)
    else:
        while inteiro.isnumeric() != True:
            inteiro = str(input('Digite um numero:'))
    print(f'Seu numero é {inteiro}')


i(input('Digite um numero:'))