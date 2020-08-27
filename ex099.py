def valor(*n):
    maior = 0
    print('-' * 30)
    print('Analisando valores')
    if len(n) == 0:
        print('Voce não passou valor')
    else:
        print(f'{n} foram informados {len(n)} ao todo')
        for k,i in enumerate(n):
            if k == 0:
                maior = n[k]
            else:
                if n[k] > maior:
                    maior = n[k]
        print(f'O maior valor é {maior}')


valor(1,2,4,5,6,3)
valor(1,4,45,7,75,65,3,3,5,63,5,2,4,6,45)
valor()
