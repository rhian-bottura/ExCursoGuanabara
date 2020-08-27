
p = float(input('Qual seu peso?'))
a = float(input('Qual sua altura'))
imc = p/(a**2)
print('O IMC DESSA PESSOA É {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <=25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc > 30 and imc <= 40:
    print('Obesidade')
else:
    print('Nivel feijuca')