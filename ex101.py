from datetime import date
def voto(nasc):
    atual = date.today().year
    nasc = atual - nasc
    if nasc >= 18 and nasc < 65:
        print(f'Com {nasc} anos: Voto Obrigatório')
    elif nasc < 18:
        print(f'Com {nasc} anos: Não vota')
    else:
        print(f'Com {nasc} anos: Voto opcional')


#principal
n = int(input('Data de nascimento:'))
voto(n)
