from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador 1 ': randint(1,6),
        'Jogador 2 ': randint(1,6),
        'Jogador 3 ': randint(1,6),
        'Jogador 4 ': randint(1,6)
}
ranking =list()
for k,v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('Ranking')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar : {v[0]} com {v[1]}')
    sleep(0.5)
