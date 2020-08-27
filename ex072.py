n = int(input('Digite um número entre 0 e 20:'))
num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
'nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete'
'dezoito','dezenove','vinte')

while n > 20 or n < 0:
    n = int(input('Tente novamente.Digite um número entre 0 e 20:'))
c = n
if n == 20:
    c = 19
print(num[c])
