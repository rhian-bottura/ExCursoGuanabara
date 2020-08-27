a1 = float(input('Digite o primeiro termo:'))
r = float(input('Digite a razão:'))
c = 1
while c != 11:
    pa = a1+(c-1)*r
    print('{} º termo  tem valor de {}'.format(c,pa))
    c+=1