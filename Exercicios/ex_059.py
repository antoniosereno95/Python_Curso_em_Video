n1 = int(input('n1: '))
n2 = int(input('n2: '))
op = int(0)
while op != 5:
    print('\n1-soma\n2-mutiplica\n3-maior\n4-novos numeros\n5-encerrar o programa')
    op = int(input('digite sua escolha: '))
    if op==1:
        print(n1+n2)
    elif op==2:
        print(n2*n1)
    elif op==3:
        if n1>n2:
            print(n1)
        else:
            print(n2)
    elif op==4:
        print('digite os novos numeros:')
        n1 = int(input('n1: '))
        n2 = int(input('n2: '))
    elif op==5:
        print('ate mais.')

print('...')