s = 0
for c in range(0,6):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        s += n
print('Soma apenas dos numeros pares = {}'.format(s))