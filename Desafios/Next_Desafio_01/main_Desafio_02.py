
def abreArquivo(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        print('arquivo nao encontrado')
    else:
        print('Arquivo encontrado com sucesso =)')


def primeiralista(nome):
    a = open(nome, 'rt')
    lista1 = []
    for linha in a:
            lista1.append(linha.replace('\n','').split(','))
    lista1.pop(0)
    return lista1


def nomecandidatos(lista):
    nomes = []
    for i in range(len(lista)):
        nome = lista[i][2]
        if nome not in nomes:
            nomes.append(nome)
    return nomes


def votosKhan(lista):
    soma = 0
    for linha in lista:
        if 'Khan' in linha:
            soma+=1
    return soma


def votosCorrey(lista):
    soma = 0
    for linha in lista:
        if 'Correy' in linha:
            soma += 1
    return soma


def votosLi(lista):
    soma = 0
    for linha in lista:
        if 'Li' in linha:
            soma += 1
    return soma


def votosOTooley(lista):
    soma = 0
    for i in range(len(lista)):
        nome = lista[i][2]
        if nome != 'Khan' and nome != 'Li' and nome != 'Correy':
            soma += 1
    return soma


def porcentagens(lista , khan , correy , li , otooley):
    t_votos = len(lista)

    por_khan = float(khan*100)/t_votos
    por_correy = float(correy*100)/t_votos
    por_li = float(li*100)/t_votos
    por_otooley = float(otooley*100)/t_votos

    lista_por =[]
    lista_por.append(por_khan)
    lista_por.append(por_correy)
    lista_por.append(por_li)
    lista_por.append(por_otooley)

    return lista_por


def vencedor(lista_por):
    maior = 0
    cont = 0
    index = int
    ganhou = ''
    for i in lista_por:
        if i > maior:
            maior = i
            index = cont
        cont += 1
    if index == 0:
        ganhou = 'Khan'
    elif index == 1:
        ganhou = 'Correy'
    elif index == 2:
        ganhou = 'Li'
    elif index == 3:
        ganhou = 'O\'tooley'

    eleito = []
    eleito.append(ganhou)
    eleito.append(maior)

    return eleito


def procuraArquivoResultado():
    nome = 'resultado.txt'
    try:
        b = open(nome, 'rt')
        b.close()
    except:
        print('arquivo nao encontrado, vou criar um para voce =)')
        criaArquivoResultado(nome)
        print('feito!')
    else:
        print(f'arquivo {nome} encontrado com sucesso =)')


def criaArquivoResultado(nome):
    try:
        b = open(nome, 'wt+')
        b.close()
    except:
        print('houve um probrema na criaçao do arquivo')
    else:
        print(f'arquivo {nome} criado com sucesso =)')


def escreveResultado(tam , lista_porcentagens , khan , correy , li ,oTooley , v):
    nome = 'resultado.txt'
    with open(nome,'w') as arquivo:
        arquivo.write('-' * 40)
        arquivo.write('\n')
        txt = 'Resultados eleitorais'
        arquivo.write(txt.center(40))
        arquivo.write('\n')
        arquivo.write('-' * 40)
        arquivo.write('\n')
        arquivo.write(f'Total de votos: {tam}\n')
        arquivo.write('-' * 40)
        arquivo.write('\n')
        arquivo.write(f'Khan: {lista_porcentagens[0].__round__(2)} ({khan})\n')
        arquivo.write(f'Correy: {lista_porcentagens[1].__round__(2)} ({correy})\n')
        arquivo.write(f'Li: {lista_porcentagens[2].__round__(2)} ({li})\n')
        arquivo.write(f'O\'Tooley: {lista_porcentagens[3].__round__(2)} ({oTooley})\n')
        arquivo.write('-' * 40)
        arquivo.write('\n')
        arquivo.write(f'Vencedor: {v[0]}\n')
        arquivo.write('-' * 40)

    with open(nome) as arquivo:
        print(arquivo.read())


#main
arq = 'dados_elecao.txt'
abreArquivo(arq)
lista = primeiralista(arq)
#print(lista[0])

#letra a
tam = len(lista)
print(f'O número total de votos expressos {tam}')

#letra b
candidatos = nomecandidatos(lista)
print(f'lista de candidatos: {candidatos}')

#letra c porcentagem de cada candidato
khan = votosKhan(lista)
correy = votosCorrey(lista)
li = votosLi(lista)
oTooley = votosOTooley(lista)
lista_porcentagens = porcentagens(lista, khan=khan, correy=correy, li=li, otooley=oTooley)
print(f'lista de porcentagens: {lista_porcentagens}')

#letra d
print(f'votos pro khan = {khan}')
print(f'votos pro Correy = {correy}')
print(f'votos pra Li = {li}')
print(f'votos pro O\'Tooley = {oTooley}')

#letra e
v = vencedor(lista_porcentagens)
print(f'O vencedor foi {v[0]} com um total de {v[1]} porcento dos votos')

#letra f
print('-'*40)
txt = 'Resultados eleitorais'
print(txt.center(40))
print('-'*40)
print(f'Total de votos: {tam}')
print('-'*40)
print(f'Khan: {lista_porcentagens[0].__round__(2)} ({khan})')
print(f'Correy: {lista_porcentagens[1].__round__(2)} ({correy})')
print(f'Li: {lista_porcentagens[2].__round__(2)} ({li})')
print(f'O\'Tooley: {lista_porcentagens[3].__round__(2)} ({oTooley})')
print('-'*40)
print(f'Vencedor: {v[0]}')
print('-'*40)

#exportar arquivo resultado
procuraArquivoResultado()
escreveResultado(tam=tam, lista_porcentagens=lista_porcentagens , khan=khan, correy=correy, li=li , oTooley=oTooley , v=v)