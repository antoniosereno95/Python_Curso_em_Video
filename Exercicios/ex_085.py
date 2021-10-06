lista=list()
impar=list()
par=list()

for i in range(7):
    n = int(input('numero:'))
    if n%2==0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
lista.append(par[:])
lista.append(impar[:])
print(lista)




