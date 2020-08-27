frase = str(input('digite a frase:')).strip().upper()
palavras = frase.replace(' ','')
inverso = ''
for letra in range(len(palavras) -1,-1,-1):
   inverso += palavras[letra]
if inverso == palavras:
    print('é palindromo')
else:
    print('Não é')