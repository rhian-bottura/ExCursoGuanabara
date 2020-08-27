aluno = dict()
nome = str(input('Nome:'))
aluno['nome'] = nome
media = float(input(f'A media de {nome}:'))
aluno['media'] = media
print('-=' * 30)
print(f'Nome:{aluno["nome"]}')
print(f'media:{aluno["media"]}')
if aluno['media'] >= 7:
    print('Situação : aprovado')
else:
    print('Situação: reprovado')
