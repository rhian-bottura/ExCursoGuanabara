lista = list()
par = list()
impar = list()
sair = ''
while True:
    if sair.upper() == 'N':
        break
    valor = int(input('Digite um valor:'))
    lista.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
    sair = input('Deseja continuar?[S/N]').upper()
    while sair not in 'SN':
        sair = input('Deseja continuar?[S/N]').upper()
print(f'Lista Total : {lista}')
print(f'Lista Pares : {par}')
print(f'Lista Impares : {impar}')
