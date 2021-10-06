
lista = []
while True:
    n = input('digite um numero: ')
    while int(lista.count(n))>=1:
        n = input('numero ja existente, tente novamente: ')
    lista.append(n)
    print('numero add com sucesso.')
    print(lista)
    resp = str(input('deseja continuar[s/n]:')).lower()
    while resp!='n' and resp !='s':
        resp = str(input('deseja continuar[s/n]:')).lower()
    if resp == 'n':
        print(f'\nlista final: {lista}')
        break









