p = ('um', 'aprender', 'gostar', 'amar', 'paixao', 'comer')
for pa in p:
    print(f'\n Na palavra {pa.upper()} temos ', end='')
    for letra in pa:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
