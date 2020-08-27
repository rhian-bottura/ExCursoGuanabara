from math import hypot
co = float(input('Cateto oposto:'))
ca = float(input('cateto adjacente:'))
h = hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(h))