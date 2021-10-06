import random

def sorteia():
    print('~'*60)
    l = list()
    for i in range(5):
        k = random.randint(1,101)
        l.append(k)
    print(f'A lista sorteada foi ', end='')
    for i in l:
        print(f'{i} ',end='')
    print()
    print('~'*60)
    return l


def somapar(lista):

    soma = 0
    for i in lista:
        if int(i)%2==0:
            soma += i
    print(f'somando o svalores pares da lista {lista} temos {soma}')
    print('~'*60)

#main
li = sorteia()
somapar(li)






