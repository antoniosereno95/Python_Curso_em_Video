def escreva(txt):
    k = len(txt)
    if int(k)%2==0:
        k +=4
    else:
        k+=3
    print('~'*k)
    print(f'  {txt}  ')
    print('~'*k)


#main
l = str(input('digite um texto: '))
escreva(l)










