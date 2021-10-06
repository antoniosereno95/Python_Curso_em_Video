
lista = list()
dados = list()
while True:
    nome = input('nome: ')
    nota1 = input('nota 1: ')
    nota2 = input('nota 2: ')
    dados.append(nome)
    dados.append(nota1)
    dados.append(nota2)
    lista.append(dados[:])
    dados.clear()
    resp = str(input('deseja continuar[s/n]: ')).lower()
    if resp == 'n':
        break
print('--' * 20)
print(f'numero --- nome ----- media')
for i in range(len(lista)):
    media = (float(lista[i][1])+float(lista[i][2]))/2
    print(f'{i} ..... {lista[i][0]} ..... {media}')
print('--' * 20)

while True:
    print('-+-' * 20)
    n = int(input('deseja ver algum boletim em expecifico?(999 para terminar)'))
    print(len(lista))
    if n >= len(lista):
        print('indice de aluno nao encontrado.')
        print('-+-' * 20)
    elif n == 999:
        print('Encerrando...')
        print('-+-' * 20)
        break
    else:
        print('-+-' * 20)
        media = (float(lista[n][1]) + float(lista[n][2])) / 2
        print(f'{lista[n][0]} ..... {media}')
        print('-+-' * 20)








