import random
n1 = random.randint(0,5)
n2 = int(input('Tente adivinha qual numero o pc pensou entre 0 a 5:'))
if n1 == n2:
    print('Monstro sagrado conseguiu,vencedor')
else:
    print('Não foi dessa vez,perdedor')
