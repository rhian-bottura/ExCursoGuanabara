from ex109 import moeda

p = float(input('Digite um numero:'))
print(f'A metade do numero {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'o dobr0 do numero {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentar o numero {moeda.moeda(p)} é {moeda.aumentar(p,10)}')
print(f'Diminuir o numero {moeda.moeda(p)} é {moeda.diminuir(p,13)}')