from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criarArquivo(arq)
cabeçalho('SISTEMA DE ARQUIVOS')



while True:
    res = menu(['-Listar Pessoas','-Cadastrar Pessoas','-Sair do sistema'])
    if res == 4:
        cabeçalho('Saindo do sistema')
        break
    elif res == 2:
        cabeçalho('NOVO CADASTRO')
        nome =str(input('Nome:'))
        idade = int(input('Idade:'))
        cadastrar(arq,nome,idade)

    elif res == 3:
        cabeçalho('OPÇÃO 3')
    elif res == 1:
        # listar conteudo
        lerArq(arq)
    sleep(2)
