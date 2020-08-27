s = 0
n = int(input('Digte um numero:'))
for c in range(1,n+1):

    if n % c == 0:
        print('\033[34m', end='')
        s += 1
    else:
        print('\033[m', end='')
    print('{}'.format(c), end='')

if s == 2:
    print(' \n \033[mPrimo')
else:
    print(' \n \033[mNão é primo')