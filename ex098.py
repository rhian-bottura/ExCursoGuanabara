from time import sleep
def contador(i,f,p):
    print(f'Contagem de {i} ate {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p =1
    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont +=p
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ',end='',flush=True)
            sleep(0.5)
            cont -= p
        print('Fim')

#programa principaç
contador(1,10,1)
contador(10,0,2)
print('Personalizar')
ini = int(input('Inicio:'))
fim = int(input('Fim:'))
pa = int(input('Passo:'))
contador(ini,fim,pa)





