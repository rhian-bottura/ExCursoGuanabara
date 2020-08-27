print('Soma e contagem de numeros: \n pare digitando 999')
n = int(input('Digite um numero:'))

cont = 0
soma= 0
while True:
    if n == 999:
        break
    soma += n
    n = int(input('Digite um numero:'))
    cont += 1

print('{} numeros somados deram {}'.format(cont,soma))