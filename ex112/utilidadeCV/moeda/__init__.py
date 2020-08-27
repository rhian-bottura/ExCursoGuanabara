def metade(v, show=True):
    v = v / 2
    if show == True:
        return moeda(v)
    else:
        return v


def dobro(v, show=True):
    v = v * 2
    if show == True:
        return moeda(v)
    else:
        return v


def aumentar(v, p, show=True):
    p = p / 100
    v = v * (1 + p)
    if show == True:
        return moeda(v)
    else:
        return v


def diminuir(v, p, show=True):
    p = p / 100
    v = v * (1 - p)
    if show == True:
        return moeda(v)
    else:
        return v


def moeda(v):
    v = str(f'R${v:.2f}')
    return v
def resumo(v,a,d):
    print('-' * 40)
    print(f'{"Resumo do valor":^30}')
    print('-' * 40)
    print(f'Preço Analisado{"":<2}:{"":<10} {moeda(v)}')
    print(f'Dobro do Preço{"":<3}:{"":<10} {dobro(v)}')
    print(f'Metade do Preço{"":<2}:{"":<10} {metade(v)}')
    print(f'Aumento de {a}%{"":<3}:{"":<10} {aumentar(v,a)}')
    print(f'Dimuição de {d}%{"":<2}:{"":<10} {diminuir(v,d)}')
    print('-' * 40)