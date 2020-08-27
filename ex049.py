n = int(input('Digite o numero da tabuada:'))
print('-=' * 10)
print('-=' * 5,'Tabuada','-=' * 5)
print('-=' * 10)
for c in range(1,11):
    s = n * c
    print('{} x {} = {}'.format(n,c,s))
    print('-=' * 10)