from datetime import date
ano = int(input('qual sua data de nascimento?'))
atual = date.today().year
idade = atual - ano
if idade <= 9:
    print('MIRIM COM IDADE DE {} ANOS'.format(idade))
elif idade <= 14:
    print('INFANTIL COM IDADE DE {} ANOS'.format(idade))
elif idade <= 19:
    print('JUNIOR COM IDADE DE {} ANOS'.format(idade))
elif idade == 20:
    print('SÊNIOR COM IDADE DE {} ANOS'.format(idade))
else:
    print('MASTER COM IDADE DE {} ANOS'.format(idade))
