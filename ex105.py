def nota(*num,show = False):
    n = dict()
    n['total'] = len(num)
    n['maior'] = max(num)
    n['menor'] = min(num)
    n['media'] = sum(num)/len(n)

    if show == True:
        if n['media'] < 6:
            n['Situaçã0'] = 'Lascado'
        elif n['media'] >= 6 and n['media'] <=8:
            n['situação'] = 'razoavel'
        else:
            n['situação'] = 'deitou'
    return n



print(nota(10,5,show=True))