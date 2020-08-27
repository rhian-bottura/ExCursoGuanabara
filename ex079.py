sair = ''
lista = list()
while True:

    if sair.upper() == 'N':
        break
    valor = int(input('Digite um valor:'))
    if valor not in lista:
        lista.append(valor)
        print('Valor Adicionado com sucesso')
    else:
        while valor in lista:
            print('Valor ja existente')
            valor = int(input('Digite um novo valor:'))
        lista.append(valor)
    sair = input('Deseja Continuar?[S/N]')
    while sair.upper() not in 'NS':
        sair = input('Deseja Continuar?[S/N]')
lista.sort()
print(lista)


