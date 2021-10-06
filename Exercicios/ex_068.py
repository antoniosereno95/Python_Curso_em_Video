import random
vitoria = True
cont = 0
while vitoria:
    j = int(input('digite um numero: '))
    pi = str(input('Par ou Impar[P/I]: ')).lower()
    while pi!='p' and pi!='i':
        pi = str(input('tente novamente[P/I]')).lower()
    r = random.randint(1,101)
    if r%2==0 and j%2==0 and pi =='p':
        cont += 1
        print('Venceu')
    elif r%2!=0 and j%2!=0 and pi =='i':
        cont += 1
        print('Venceu')
    else:
        if cont!=0 :
            print('Perdeu, ',cont,' vitorias consecutivas')
            break
        else:
            print('Perdeu.')
            break









