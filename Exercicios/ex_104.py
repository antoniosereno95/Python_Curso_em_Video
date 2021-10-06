
def leiaint(p):
    flag = False
    valor = 0
    while True:
        n = str(input(f'{p}'))
        if n.isnumeric():
            flag = True
            valor = int(n)
        else:
            print('erro, digite um numero inteiro.')
        if flag == True:
            return valor
            break


#main
n = leiaint('digite um numero: ')
print(f'voce acabou de digitar o numero {n}')