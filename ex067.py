print('-=' * 10)
print('-=' * 5, 'Tabuada', '-=' * 5)
print('-=' * 10)
n = 0

while True:
    if n < 0:
        break
    n = int(input('Digite o numero desejado:'))
    v = 0
    while v < 10:
        if n < 0:
            break
        v += 1
        s = n * v
        print('{} x {} = {}'.format(n, v, s))
        print('-=' * 10)


print('Tabuada Finalizada')
