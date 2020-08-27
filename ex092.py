from datetime import date
emprego = dict()

nome = str(input('Nome:'))
nasc = int(input('Data de nascimento:'))
carteira = int(input('Carteira de trabalho(0 não tem):'))
emprego['nome'] =  nome
atual = date.today().year
idade = atual - nasc
emprego['idade'] = idade
emprego['ctps'] = carteira
if emprego['ctps'] == 0:
    print(f'Nome:{emprego["nome"]}')
    print(f'Idade:{emprego["idade"]}')
    print(f'ctps: {emprego["ctps"]}')
else:
    contrato = int(input('Ano de contratação:'))
    salario = float(input('Salario R$ '))
    emprego['contrato'] = contrato
    emprego['salario'] = salario
    aposenta = (contrato + 35) - nasc
    print(f'Nome:{emprego["nome"]}')
    print(f'Idade:{emprego["idade"]}')
    print(f'ctps: {emprego["ctps"]}')
    print(f'Ano de contratação:{emprego["contrato"]}')
    print(f'Salario R$ {salario:.2f}')
    print(f'aposentadoria {aposenta}')


print(emprego)
