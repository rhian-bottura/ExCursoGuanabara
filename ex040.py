n1 = float(input('Primeira nota:'))
n2 = float(input('Segunda nota:'))
m = (n1+n2)/2
if m < 5:
    print('REPROVADO COM MÉDIA DE {}'.format(m))
elif m >=5 and m <=6.9:
    print('RECUPERAÇÃO COM MEDIA DE {}'.format(m))
else:
    print('APROVADO COM MÉDIA DE {}'.format(m))