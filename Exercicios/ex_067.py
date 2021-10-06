while True:
    print('----------------------------------------')
    n = int(input('quer ver a tabuada de qual valor? '))
    print('----------------------------------------')
    if n < 0:
        print('Encerrando o programa.')
        print('----------------------------------------')
        break
    for i in range(11):
        print(n,' X ',i,' = ',n*int(i))









