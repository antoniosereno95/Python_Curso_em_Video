d = dict()
lista = list()
w=0
while True:
    w+=1
    d['nome'] = str(input(f'nome {w}: '))
    sexo = str(input(f'sexo[M/F] {w}: ')).lower()
    while sexo!='m' and sexo!='f':
        sexo = str(input(f'sexo[M/F] {w}: ')).lower()
    d['sexo'] = str(sexo)
    d['idade'] = int(input(f'idade {w}: '))
    lista.append(d.copy())
    resp = str(input('deseja continuar[s/n]')).lower()
    if resp == 'n':
        break
print(lista)
print('---RESPOSTAS---')
print(f'Letra a: total de pessoas cadastradas foi de {len(lista)}')
soma_id = 0
for index_lista,dic in enumerate(lista):
    #esse for pega os index da lista e os valores
    #que estao no dicionario, dai a variavel 'dic'
    #equivale ao mini dicionario que esta em cada
    #index da lista =)
    soma_id += dic['idade']
media_id = float(float(soma_id)/len(lista))
print(f'Letra b: a media de idade do grupo é {media_id}')

mulheres = list()
for index_lista,dic in enumerate(lista):
    if str(dic['sexo'])=='f':
        m = str(dic['nome'])
        mulheres.append(m)
print('Letra c: Lista com os nomes de todas as mulheres presentes no grupo.')
for j in mulheres:
    print(f'{j}')
print('FIM da lista de mulheres')

ac_media = list()
for index,dic in enumerate(lista):
    if float(dic['idade']) > media_id:
        n = str(dic['nome'])
        ac_media.append(n)
print('Letra d: lista com os nome dos participantes com idade acima da media:')
for i in ac_media:
    print(f'{i}')
print('Fim da lista de pessoas acima da media')





