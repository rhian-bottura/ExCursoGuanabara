v = float(input('velocidade do automovel:'))
if v > 80:
    conta = (v-80) * 7
    print('Foi multado por R${}'.format(conta))
print('Sua velocidade foi de {}km'.format(v))