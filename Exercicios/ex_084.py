
lista =[]
dados =[]
resp = ''
while resp != 'n':
    nome = str(input('nome: '))
    peso = int(input('peso: '))
    dados.append(nome)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    resp = str(input('continuar[s/n]')).lower()
print(lista)
print(f'letra a: {len(lista)}')

maior_peso = int(0)
maior_nomes =[]
for i in lista:
    if i[1] > maior_peso:
        maior_peso = i[1]
for i in lista:
    if i[1] == maior_peso:
        maior_nomes.append(i[0])

menor_peso = int(300)
menor_nomes = []
for i in lista:
    if i[1] < menor_peso:
        menor_peso = i[1]
for i in lista:
    if i[1] == menor_peso:
        menor_nomes.append(i[0])

print(f'letra b: o maior peso foi de {maior_peso}, pertencente aos participantes {maior_nomes}')
print(f'letra c: o menor peso foi de {menor_peso}, pertencendo aos participantes {menor_nomes}')
