from datetime import date
atual = date.today().year
s = 0
a = 0
for c in range(0,7):
    ano = int(input('Qual sua data de nascimento:'))
    if atual - ano >= 18:
        s+= 1
    else:
        a+=1
print('{} Pessoas são maiores de idade'.format(s))
print('{} Pessoas são menores de idade'.format(a))