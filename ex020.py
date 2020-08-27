import  random
n1 =str(input('primeiro aluno:'))
n2 = str(input('segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1,n2,n3,n4]
e = random.shuffle(lista)
print('A ordem de apresentação sera')
print(lista)