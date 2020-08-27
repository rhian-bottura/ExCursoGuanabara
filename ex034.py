from math import trunc
s = float(input('Salario'))
if s > 1250:
    a = s * 1.10
else:
    a = s * 1.15
print('O salario com o aumento é {}'.format(a.trunc()))
