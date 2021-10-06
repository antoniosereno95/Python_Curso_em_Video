
tupla = tuple(input('digite: ') for i in range(4))

print('letra a: ',tupla.count('9'))
print('letra b: ',tupla.index('3'))
c = 0
for k in tupla:
    if int(k)%2==0:
        c +=1
print('letra c: ',c)






