cont18 = 0
contH = 0
contM = 0
continuar = ''
while True:
    print('-----------------Cadastrando---------------------')
    idade = int(input('Qual sua idade?'))
    sexo = str(input('Qual seu sexo?[M/F]')).upper()
    while sexo not in 'FM':
        sexo = str(input('Qual seu sexo?[M/F]')).upper()

    if idade > 18:
        cont18 +=1
    if sexo == 'M':
        contH +=1
    if sexo == 'F' and idade < 20:
        contM +=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N]')).upper()
    if continuar == 'N':
        break
print(f'{cont18} Pessoa com mais de 18')
print(f'{contH} Homens cadastradas')
print(f'{contM} Mulheres menores de 20 anos cadastradas')

