print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)
lista = ('Pão',1,'Batata',2,'Cachaça',5)
for c in range(0,len(lista),2):
    print(f'{lista[c]:.<30} R$ {lista[c+1]}')
print('=' * 40)

