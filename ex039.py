a = int(input('Qual sua idade?'))
i = 2020 - a
print('Quem nasceu em {} ja esta com {} anos'.format(a, i))
if i < 18:
    t = 18 - i
    print('Voce ainda vai se alistar daqui a {} anos'.format(t))
    print('Vai ter que se alistar em {}'.format(2020 + t))
elif i > 18:
    t = i - 18
    print('Voce ja passou {} anos de se alistar'.format(t))
    print('Seu alistamento foi em {}'.format(2020 - t))
else:
    print('Ta na hora de se alistar')
