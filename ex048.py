s=0
s1=0
for c in range(1,501):
    if c % 2 !=0:
        if c % 3  ==0:

            s+=c
            s1 +=1
print('A Somatoria dos {} numeros impares multiplos de tres é igual a {}'.format(s1,s))