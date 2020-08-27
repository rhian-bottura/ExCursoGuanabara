nome = str(input('Digite seu nome')).strip()
print(nome.upper())
print(nome.lower())

print(len(nome.replace(" ","")))
lista = nome.split()
print(len(lista[0]))