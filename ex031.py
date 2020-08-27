d = float(input('qual a distancia da viagem em km?'))
if d <= 200:
    p = d * 0.50
else:
    p = d * 0.45
print('Valor da passagem é igual a R$ {}'.format(p))