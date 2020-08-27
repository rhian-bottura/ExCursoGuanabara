l = int(input('qual a largura?'))
a = int(input('qual a altura?'))
area = l * a
t = area / 2
print('para pintar uma area de {} m² o pintor precisa de {:.2f}L de tinta '.format(area,t))