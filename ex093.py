from time import sleep
jogador = dict()
gols =list()
total = 0
nome = str(input('Nome do jogador:'))
partidas = int(input(f'Quantas partidas {nome} jogou ? '))
jogador['nome'] = nome
for c in range(0,partidas):

    gol = int(input(f'Quantos gols na {c+1} º Partida:'))
    gols.append(gol)
    total += gol
    jogador['gols'] = gols.copy()
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
print(f'Nome:{jogador["nome"]}')
print(f'Gols:{gols}')
print(f'Total:{jogador["total"]}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for c in range(0,partidas):
    print(f'{ "=>":>10}Na {c+1} º Partida,fez {gols[c]} gols')
    sleep(0.5)
print(f'total:{jogador["total"]}')


