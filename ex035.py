r1 = float(input('reta1:'))
r2 = float(input('reta2:'))
r3 = float(input('reta3:'))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[0:33:41m forma Triângulo')
else:
    print('Não forma triangulo')
