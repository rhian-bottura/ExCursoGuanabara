from math import  sin,cos,tan,radians
a = float(input('Qual o angulo'))
sen = sin(radians(a))
cos = cos(radians(a))
ta = tan(radians(a))
print('O angulo {} tem: \n seno = {:.2f} \n cosseno = {:.2f}\n Tangente = {:.2f}'
      .format(a,sen,cos,ta)
      )