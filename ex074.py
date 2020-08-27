from random import randint
sorteo = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
maior = 0
menor = 0
print('Os numeros sorteados foram',end='')
for c in sorteo:
    print(f'{c} ',end='')

print(f'\nO maior numero foi {max(sorteo)}')
print(f'O menor numero foi {min(sorteo)}')