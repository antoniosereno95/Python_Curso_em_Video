
def notas(* nota,sit=False):
    maior = 0
    menor = 1000
    soma = 0
    d = dict()
    for i in nota:
        if int(i) > maior:
            maior = int(i)
        if int(i) < menor:
            menor = int(i)
        soma += int(i)
    media = float(soma)/len(nota)
    d['total'] = len(nota)
    d['maior'] = maior
    d['menor'] = menor
    d['media'] = media
    if sit == True:
        if media < 6.0:
            d['situaçao'] = 'ruim'
        elif media >=6.0 and media < 7.0:
            d['situaçao'] = 'razoavel'
        elif media >=7.0 and media <8.0:
            d['situaçao'] = 'boa'
        elif media >= 8.0:
            d['situaçao'] = 'otima'
    return d

#main
n = notas(5,8,sit=True)
print(n)