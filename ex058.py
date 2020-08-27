import random
ten = 1
pc = random.randint(1,10)
print('Tente acertar o numero que o computador pensou!!! de 0 a 10')
p = int(input('Tente acertar o numero:'))
while p != pc:
    p = int(input('Tente acertar o numero:'))
    ten +=1
print('Parabens você conseguiu, com {} tentativas'.format(ten))
print('Computador jogou {}'.format(pc))
