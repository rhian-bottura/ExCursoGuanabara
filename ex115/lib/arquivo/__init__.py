
from ex115.lib.interface import *

def arquivoexiste(nome):
    try:
        a = open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a = open(nome,'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]} {dado[1]} Anos')
    finally:
        a.close()


def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq,'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever no arquivo')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
