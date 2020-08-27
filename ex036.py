print('='*20)
print('{:^10}'.format('Emprestimo'))

vcasa = float(input('Valor da Casa:'))
s = float(input('Seu Salario:'))
a = int(input('Em quantos anos deseja pagar:'))
mensal = vcasa / (a * 12)
s2 = s * 0.30
if mensal > s2:
    print('Emprestimo negado')
else:
    print('Emprestimo aceito')
