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
