pessoa = dict()
cadastro = list()
sair = ''
m = 0
while True:
    if sair == 'N':
        break
    nome = str(input('Nome:'))
    sexo = str(input('Sexo[M/F]:')).upper()
    while sexo not in 'FM':
        sexo = str(input('Sexo[M/F](valido):')).upper()
    idade = int(input('Idade:'))
    pessoa['nome'] = nome
    pessoa['sexo'] = sexo
    pessoa['idade'] = idade
    cadastro.append(pessoa.copy())
    pessoa.clear()
    sair = str(input('Deseja continuar?[S/N]')).upper()
    while sair not in 'SN':
        sair = str(input('Deseja continuar?[S/N]')).upper()
    m += idade

me = m / len(cadastro)
print('-=' * 30)
print(f'-O grupo tem {len(cadastro)} pessoas')
print(f'-A media de idade é {me} anos')
print('-A mulheres cadastradas foram :', end=' ')
for k, v in enumerate(cadastro):
    if cadastro[k]['sexo'] in 'Ff':
        print(cadastro[k]['nome'], end=' ')

print('\n-A lista das pessoas que estão acima da média:')
for k, v in enumerate(cadastro):
    if cadastro[k]['idade'] > me:
        print(f'-Nome = {cadastro[k]["nome"]};', end='')
        print(f'sexo = {cadastro[k]["sexo"]};', end='')
        print(f'idade = {cadastro[k]["idade"]}')
        print()

print('<< ENCERRADO >>')
