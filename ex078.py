lista = list()
for c in range(0,5):
    lista.append(int(input(f'Digite um valor para posição {c}:')))
maior = max(lista)
menor = min(lista)
print(f'Voce digitou os valores {lista}')

print(f'O maior valor digitado foi {maior} na posição ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O Menor valor digitado foi {menor} na posição ',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')