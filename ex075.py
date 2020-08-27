n1 = int(input('Valor:'))
n2 = int(input('Valor:'))
n3 = int(input('Valor:'))
n4 = int(input('Valor:'))
num = (n1,n2,n3,n4)

print(f'O numero nove apareceu {num.count(9)} vezes')
print('Os Seguintes valores são pares: ',end='')
for c in num:
    if c % 2 ==0:
        print(f'{ c }', end='')
if 3 in num:
    print(f'\nO primeiro valor de 3 digitado na {num.index(3) + 1} º posição')
else:
    print('\nValor 3 não foi digitado')