from random import randint
lista = list()
par = list()
def sortea():
    print(f'Sorteando  5 valores',end=' ')
    for c in range(0,5):
        lista.append(randint(1,6))
        print(lista[c],end=' ')
    print()

def soma(l):
    soma = 0
    for c in range(0,5):
        if lista[c] % 2 == 0:
            soma += lista[c]
            par.append(lista[c])


    print(f'Somando os valores pares{par} temos {soma}')


sortea()
soma(lista)

