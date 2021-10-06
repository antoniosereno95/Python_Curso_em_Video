#modulos lib.arquivo

def cabecalho(txt):
    print('-'*42)
    print(txt.center(42))
    print('-'*42)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um erro na criaçao do aquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('erro ao ler o arquivo.')
    else:
        cabecalho('Pessoas Cadastradas')
        #print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')

    finally:
        a.close()


def cadastrar(arq , nome='<desconhecido>' , idade =0):
    try:
        a = open(arq, 'at')
    except:
        print(f'houve um erro ao abrir o arquivo {arq}')
    else:
        try:
            a.write(f'\n{nome};{idade}')
        except:
            print('erro ao tentar escrever no arquivo')
        else:
            print('Novo registro concluido com sucesso.')
            a.close()


