pa = int(input('Digite o primeiro termo da PA:'))
r = float(input('Digite a razão da PA'))
for c in range(1,11):
  p = pa+(c-1)*r
  print(' {}'.format(p),end='->')