from random import randint
sorteios = list()
dados =list()
print('-'*40)
print(f'{"MEGA SENA ":^40}')
print('-'*40)
n = int(input('Quantos jogos você quer que eu sorteie:'))
print(f'{"SORTEANDO OS  JOGOS":-^40}')
for c in range(0,n):
    for p in range(0,6):
        sorteios.append( randint(1,60))
    sorteios.sort()
    print(f'Jogo {c + 1} :{sorteios}')
    sorteios.clear()
