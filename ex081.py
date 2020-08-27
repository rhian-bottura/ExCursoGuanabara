sair =''
lista = list()
while True:
    if sair.upper() == 'N':
        break
    lista.append(int(input('Digite um valor:')))

    sair = input('Deseja continuar?[S/N]').upper()

    while sair  not in 'SN':
        sair = input('Deseja continuar?[S/N]').upper()

print(f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print(f' Valores em ordem descente: {lista}')
if  5 in lista:
    print(f'Valor 5 foi digitado e a primeira posicão dele é {lista.index(5)}')
else:
    print('5 Não está na lista')