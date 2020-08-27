i = 0
mulher = 0
velho = 0
nomeVelho = ''
homem = 0
for c in range(1,5):
    print('-'* 5, '{} º Pessoa'.format(c), '-' * 5)
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]'))
    i += idade
    if sexo.upper() == 'F' and idade < 20:
        mulher += 1
    elif sexo.upper() == 'M':
        homem += 1
        if homem ==1:
            velho = idade
            nomeVelho = nome
        else:
            if idade > velho:
                velho = idade
                nomeVelho = nome

m = i/c
print('A média de idade é {}'.format(m))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher))
print('O homem mais velho tem {} anos e se chama {}'.format(velho,nomeVelho))
