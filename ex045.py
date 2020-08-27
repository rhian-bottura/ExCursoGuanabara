import random
from time import sleep

pc = random.randint(0, 2)
itens = ['Pedra', 'Papel', 'Tesoura']
print('[0]- Pedra \n [1]-papel \n [2]-tesoura')
p = int(input('qual sua jogada?'))
print('-=' * 10)
print('JO')
sleep(1)  # ESPERA UM SEGUNDO PARA PROXIMA AÇÃO
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)  # REPETE 10 =
print('Computador jogou : {}'.format(itens[pc]))  # VETOR
print('Voce Jogou: {}'.format(itens[p]))

if pc == 0:
    if p == 0:
        print('EMPATE')
    elif p == 1:
        print('VOCÊ VENCEU')
    elif p == 2:
        print('COMPUTADOR VENCEU')
    else:
        print('JOGADA INVALIDA')
elif pc == 1:
    if p == 0:
        print('COMPUTADOR VENCEU')
    elif p == 1:
        print('VOCÊ VENCEU')
    elif p == 2:
        print('VOCÊ VENCEU')
    else:
        print('JOGADA INVALIDA')
elif pc == 2:
    if p == 0:
        print('VOCÊ VENCEU')
    elif p == 1:
        print('COMPUTADOR VENCEU')
    elif p == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA')
print('-=' * 10)
