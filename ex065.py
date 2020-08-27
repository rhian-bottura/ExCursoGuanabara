soma = 0
contador = 0
c = 'S'
maior = 0
menor = 0
while c =='S':
    n = float(input('Digite um numero:'))
    soma += n
    contador +=1
    if contador ==1 :
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    c = str(input('Deseja continuar?[S/N}')).upper()
media = soma/ contador
print('A media entre os valores foi {}'.format(media))
print('O maior valor foi {}'.format(maior))
print('O menor valor foi {}'.format(menor))