def ficha(gol,nome):
    if gol.isnumeric():
        gol = int(g)
    else:
        gol = 0
    if nome == '':
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gol} gol(s).')



n = input('Nome:')
g = input('Gols:')
ficha(g,n)