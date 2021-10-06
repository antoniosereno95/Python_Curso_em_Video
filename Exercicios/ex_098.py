def escreva(txt):
    k = len(txt)
    if int(k)%2==0:
        k +=4
    else:
        k+=3
    print('~'*k)
    print(f'  {txt}  ')
    print('~'*k)


def contador(inicio,fim,passo):
    if int(passo)==0 and int(inicio)<int(fim):
        passo = 1
    elif int(passo)==0 and int(inicio)>int(fim):
        passo = -1
    print('letra a:')
    for i in range(1,11,1):
        print(f'{i}',end=' ')
    print('\nletra b:')
    for i in range(10,0,-2):
        print(f'{i}', end=' ')
    print('\nletra c:')
    for i in range(int(inicio),int(fim)+1,int(passo)):
        print(f'{i}', end=' ')


#main
escreva('contador')
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))
contador(i,f,p)




