n = int(input('Digte numero inteiro'))
b = int(input('Escolha uma base: \n 1- binario \n 2-octal \n 3-hexadecimal:'))
if b == 1:
    print('Seu numero {} em binario é {}'.format(n, bin(n)[2:]))
elif b == 2:
    print('Seu numero {} em octal {}'.format(n, oct(n)[2:]))
else:
    print('Seu numero {} em hexadecimal {}'.format(n, hex(n)[2:]))
