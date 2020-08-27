sexo = input('Digite seu sexo[M/F]:').upper()
while sexo not in 'MmFf':
    sexo = input('Digite seu sexo[M/F]:').upper()
if sexo == 'M':
    print('Seu sexo é masculino')
else:
    print('Seu sexo é feminino')