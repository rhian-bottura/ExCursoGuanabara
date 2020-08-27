jogador = dict()
gols = list()
estatistica = list()
sair = ''

while True:
    if sair == 'N':
        break
    nome = str(input('Nome:'))
    jogador['nome'] = nome
    partidas = int(input('Partidas jogadas:'))
    total = 0
    for c in range(0, partidas):
        gol = int(input(f'Quantos gols fez na {c + 1} º Partida:'))
        gols.append(gol)
        jogador['gols'] = gols.copy()
        total += gol
    gols.clear()
    jogador['total'] = total
    sair = str(input('Deseja continuar?[S/N]:')).upper()
    while sair not in "SN":
        sair = str(input('Deseja continuar?[S/N]:')).upper()
    estatistica.append(jogador.copy())
print('cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
print('-'*50)
for k,v in enumerate(estatistica):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-' * 50)
while True:
    m = int(input('Mostrar Dados de qual jogador?'))
    if m >= len(estatistica) or m < 0:
        print(f'ERRo!Jogador com o codigo{m} Não existe Tente novamente')

    else:
        print(f'---Levantantamento do jogador {estatistica[m]["nome"]}---')

        for i, g in enumerate(estatistica[m]['gols']):
            print(f'   No jogo {i + 1} fez {g}')
    print('-' * 50)


    if m == 999:
        break
print("Volte sempre")