from ex108 import moeda

p = float(input('Digite um numero:'))
print(f'A metade do numero {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'o dobro do numero {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentar o numero {moeda.moeda(p)} é {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuir o numero {moeda.moeda(p)} é {moeda.moeda(moeda.diminuir(p,13))}')