print('-'*20)
baro = 'Magazine Luiza'
print(f'{baro:^20}')
print('-'*20)
total = 0
mais = 0
barato =0
nomebarato = ''
continuar = ''
while True:
    print('----------------Compras-----------------')
    nome = str(input('Nome do produto:'))
    preco = float(input('Preço R$'))
    total +=preco
    if preco > 1000:
        mais +=1
    if barato == 0:
        barato = preco
        nomebarato = nome
    else:
        if preco < barato:
            barato = preco
            nomebarato = nome
    continuar = str(input('Deseja continuar?[S/N]')).upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]')).upper()
    if continuar == "N":
        break
print('{:-^40}'.format(' NOTA FISCAL '))
print(f'Total gasto foi R${total}')
print(f'{mais} Produtos  com valor acima de R$1000')
print(f'O nome do produto mais barato é {nomebarato} que custa {barato}')