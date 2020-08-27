time = ('Palmeiras','Flamengo','Santos','Corinthians','São Paulo','Grémio','Internacional',
'Fluminense','Atlético PR','Chapecoense')
print('Os 5º Primeiros são:',time[0:5])
print('Os 4º ultimos são:',time[9:5:-1])
print('Em ordem Alfabética',sorted(time))
print(f'Chapecoense esta na {time.index("Chapecoense") + 1} º Posição')
