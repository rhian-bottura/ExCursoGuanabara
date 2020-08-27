def valida(msg):
    val = False
    while not val:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f"ERRO: {entrada} é um preço invalido")
        else:
            val = True
            return float(entrada)

