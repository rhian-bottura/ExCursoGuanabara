p = float(input('Preço do produto:'))
c = int(input(
    'condição de pagamento: '
    '\n 1- a vista no dinheiro/ cheque '
    '\n 2- a vista no cartão '
    '\n 3- em até 2x no cartão '
    '\n 4- em 3X ou mais no cartão:'))
print('Preço do produto normal é: {}'.format(p))
if c == 1:
    p = p * 0.90
    print('O preço final é {:.2f}'.format(p))
elif c == 2:
    p = p * 0.95
    print('O preço final é {:.2f}'.format(p))
elif c == 3:
    print('O preço final é {:.2f}'.format(p))
elif c == 4:
    parcelas = int(input('Quantas parcelas?'))
    p = p * 1.20
    par = p / parcelas
    print('Sua compra será parcelada em {}x de R${} com juros'.format(parcelas, par))
    print('O preço final é {:.2f}'.format(p))
