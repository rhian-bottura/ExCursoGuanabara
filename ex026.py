frase = input('digite uma frase:').strip().lower()
print(' a letra a foi mostado {} vezes'.format(frase.count('a')))
print('A primeira letra A aparece na posição {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu em {}'.format(frase.rfind('a')+1))