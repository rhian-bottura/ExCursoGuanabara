maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('peso da {}º pessoa:'.format(c)))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}kg'.format(maior))
print('O menor peso é {} kg'.format(menor))
