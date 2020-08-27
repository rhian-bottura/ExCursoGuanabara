pessoas = list()
dados = list()
sair =''
maior = 0
menor = 0
contador = 0
while True:
    if sair.upper() =='N':
        break
    nome = str(input('Nome:'))
    peso = float(input('Peso:'))

    dados.append(nome)
    dados.append(peso)
    if  len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    sair = str(input('Deseja continuar?[S/N]')).upper()
    while sair not in 'SN':
        sair = str(input('Deseja continuar?[S/N]')).upper()

print(f'Foram cadastradas {len(pessoas)}')
print(f'O maior peso foi {maior} kg.Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor} kg.Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')


