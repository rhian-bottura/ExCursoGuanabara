matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
somaco = 0
maior = 0
for c in range(0,3):
    for l in range(0,3):
        valor = int(input(f'Digite um valor para [{l}][{c}]'))
        matriz[c][l] = valor
        if valor % 2 == 0:
            soma += valor
        if c == 2:
            somaco +=valor
        if l == 1:
            if c == 0:
                maior = valor
            if valor > maior:
                maior = valor
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma da terceira coluna é {somaco}')
print(f'O maior valor da segunda linha é {maior}')