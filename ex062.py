a1 = float(input('Digite o primeiro termo:'))
r = float(input('Digite a razão:'))
c = 1
n = 1
while n != 11:
    pa = a1+(c-1)*r
    print('{} ->'.format(pa), end='')
    c+=1
    n+=1

    if n ==11:
        print('PAUSA')
        s = int(input('\nDeseja mais quantos termos?'))
        n -= s
print('PA finalizada')