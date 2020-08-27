r1 = float(input('reta1:'))
r2 = float(input('reta2:'))
r3 = float(input('reta3:'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print(' forma Triângulo')
    if r1 == r2 and r1 == r3:
        print('Triangulo equilatero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Triangulo isósceles')
    else:
        print('Triangulo escaleno')

else:
    print('Não forma triangulo')