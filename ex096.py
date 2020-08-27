def area(l, c):
    a = l * c
    print(f'A area de um terreno {l} x {c} é de {a} m²')


print('Controle de terrenos')
print('-' * 30)
l = float(input('LARGURA(m):'))
c = float(input('COMPRIMENTO(m)'))
area(l,c)
