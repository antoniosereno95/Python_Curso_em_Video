
def AbreArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('ERRO:arquivo nao encontrado.')
    else:
        print('arquivo encontrado =)')
        a.close()


def TotalDeMeses(nome):
    a = open(nome,'rt')
    contador = 0
    for linha in a:
        if linha !=0:#titulo do arquivo
            contador += 1
    a.close()
    return contador


def retornaLista(nome):
    a = open(nome, 'rt')
    lista = []
    for linha in a:
        lista.append(linha.replace("\n", "").split(','))

    lista2 = []
    for i in range(len(lista)):
        if i != 0:
            lista2.append(lista[i][1])

    return lista2


def ValorLiquido(lista2):
    soma = 0
    for i in range(len(lista2)):
        numero = int(lista2[i])
        soma += numero

    return soma


def media(lista):
    soma = ValorLiquido(lista)
    t = len(lista)
    m = float(soma)/t
    return m


def media_mudanca(lista3):
    soma = 0.0
    for i in range(len(lista3)):
        soma += float(lista3[i])

    mm = float(soma) / len(lista3)
    return mm


def lista_mudanca(lista):
    agr = 0
    anterior = 0
    dif = 0
    lista3 = []
    for i in range(len(lista)):
        if int(i) == 0:
            anterior = lista[i]
        if int(i) == 1:
            agr = lista[i]
        # agr começa a comparaçao
        if int(i) >= 1:
            dif = float(agr) - float(anterior)
            lista3.append(dif)
        if int(i) > 1:
            anterior = agr
            agr = lista[i]
    return lista3


def maior_auemnto(lista3):
    maior = 0.0
    for i in lista3:
        if float(i) > maior:
            maior = i
    return maior

def menor_aumento(lista3):
    menor = 1000000000.0
    for i in lista3:
        if float(i) < menor:
            menor = i
    return menor
#main
#abre o arquivo
arq = 'dados_financeiro.txt'
AbreArquivo(arq)

#letra A
total_meses = TotalDeMeses(arq)
print(f'O número total de meses incluídos no conjunto de dados: {total_meses}')

#letra B
lista = retornaLista(arq)
valor = ValorLiquido(lista)
print(f'O valor total líquido de "Lucros / Perdas" durante todo o período foi de: {valor}')

#letra c
m = media(lista)
print(f'A média dos "Lucros / Perdas" durante todo o período : {m}')

#funçao da lista de mudança que vai ser usada na letra d,e,f
lista_m = lista_mudanca(lista)

#letra d
mediaMudaça = media_mudanca(lista_m)
print(f'A média das mudanças em "Lucros / Perdas" durante todo o período foi de: {mediaMudaça}')

#letra e
maior_au = maior_auemnto(lista_m)
print(f'O maior aumento nos lucros (data e valor) durante todo o período foi {maior_au}')

#letra f
menor_au = menor_aumento(lista_m)
print(f'A maior redução nas perdas (data e valor) ao longo de todo o período foi de: {menor_au}')


