v1 = float(input('Digite o primeiro valor:'))
v2 = float(input('Digite o segunda valor:'))
escolha = 0
while escolha != 5:
    print('[1] Somar \n [2] Multiplicar \n[3] Maior \n[4]Novos numeros \n[5] sair')
    escolha = int(input('Escolha uma opção:'))

    if escolha == 1:
        soma = v1 + v2
        print('A soma de {} + {} = {}'.format(v1,v2,soma))
        print('=' * 20)
    elif escolha == 2:
        mult = v1 * v2
        print('A multiplicação de {} * {} = {}'.format(v1, v2, mult))
        print('=' * 20)
    elif escolha == 3:
        if v1 > v2:
            print('Primeiro valor é maior')
            print('=' * 20)
        else:
            print('Segundo valor é maior')
            print('=' * 20)
    elif escolha == 4:
        v1 = float(input('Digite o primeiro valor:'))
        v2 = float(input('Digite o segunda valor:'))
    elif escolha > 5:
        print('Opção invalida')
print('Programa finalizado')
