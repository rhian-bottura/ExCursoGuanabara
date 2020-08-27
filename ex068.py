from random import randint
print('-----------Bota Jogar par ou impar---------------')
pc = 0
p = 0
v = ''
vitorias = 0
while True:
    pc = randint(1, 10)
    p = int(input('Escolha um numero:'))
    v = str(input('Escolha par ou impar [I/P]')).upper()
    soma = p + pc
    if soma% 2 ==0:
        if v == 'P':
            print(f'PC jogou {pc} e você {p} e deu {p + pc} é Par')
            print('Jogador venceu')
            vitorias +=1
            print('----------Bora jogar Novamente--------------')
        else:
            break
    else:
        if v == 'I':
            print(f'PC jogou {pc} e você {p} e deu {p + pc} é Impar')
            print('Jogador venceu')
            vitorias +=1
            print('----------Bora jogar Novamente--------------')
        else:
            break
if v == 'P':
    v = 'Par'
    b = 'Impar'
else:
    v = 'Impar'
    b = 'par'
print(f'PC jogou {pc} e você {p} e deu {p+pc} é {b} você escolheu {v}')
print('Entao você perdeu')
print(f'Vitorias consecutivas {vitorias}')

