
def fatorial(n,show=False):
    fat = 1
    for i in range(int(n)+1):
        if int(i) != 0:
            fat *= i
    if show == True:
        for i in range(int(n),0,-1):
            if i != 1:
                print(f'{i} X ',end='')
            if i == 1:
                print(f'{i} ',end ='')
        print(f'= {fat}')
    else:
        print(f'{fat}')


#main
fatorial(5,True)






