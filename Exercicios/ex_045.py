import random
p = int(input('pedra(1), papel(2) ou tesoura(3): '))
#pedra = 1
#papel = 2
#tesoura = 3
r = int(random.randint(1,3))
print(r)
if p == r:
    print('empate')
elif (p==1 and r==3) or (p==2 and r==1) or (p==3 and r==2):
    print('player ganhou')
else:
    print('PC ganhou')








