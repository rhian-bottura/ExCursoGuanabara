alunos = list()
escola = list()
sair = ''
cont = 0
while True:
    if sair == 'N':
        break
    alunos.append(cont)
    cont += 1
    alunos.append(input('Nome:'))
    nota1 = float(input('Nota1:'))
    if nota1 <=10 and nota1 >=0:
        alunos.append(nota1)
    else:
        while nota1 > 10 or nota1 < 0:
            nota1 = float(input('Nota1(valida):'))
            alunos.append(nota1)
    nota2 = float(input('Nota2:'))
    if nota2 <=10 and nota2 >=0:
        alunos.append(nota2)
    else:
        while nota2 > 10 or nota2 < 0:
            nota2 = float(input('Nota2(valida):'))
            alunos.append(nota2)
    media = (alunos[2] + alunos[3])/2
    alunos.append(media)
    escola.append(alunos[:])
    alunos.clear()

    sair = str(input('Deseja continuar?[S/N]')).upper()
    while sair not in 'NS':
        sair = str(input('Deseja continuar?[S/N]')).upper()
print('='*30)
print(f'{"No.":<5}',end='')
print(f'{"NOME":<20}',end='')
print('MÉDIA')
print('='*30)
for c in range(0,cont):
    print(f'{escola[c][0]:<5} {escola[c][1]:<20} {escola[c][4]}')
print('='*30)
while True:
    m = int(input('Mostrar notas de qual aluno?'))
    if m == 999:
        break
    if m < len(escola):
        print(f'Notas de {escola[m][1]} São {escola[m][2:4]}')
    else:
        print('Aluno Invalido')


