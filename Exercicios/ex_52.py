n = int(input())
e = True
for i in range(n-1,1,-1):
    if n%int(i)==0 and i!=1:
        e = False

if e==True:
    print('é primo')
else:
    print('nao é primo')