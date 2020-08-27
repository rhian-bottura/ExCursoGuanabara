ex = input('Digite sua expressão')
cont = 0
cont2 = 0
for c in range(0, len(ex)):
    if '(' in ex[c]:
        cont += 1
    if ')' in ex[c]:
        cont2 += 1
print(cont, cont2)

if cont == cont2:
    print('Expressão válida')
else:
    print('Expressão Inválida')
