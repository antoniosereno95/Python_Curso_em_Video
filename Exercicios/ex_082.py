
lista =[]
impar =[]
par =[]

true = True
while true:
    n = input('digite um numero:')
    lista.append(n)
    resp = str(input('deseja continuar?[s/n]')).lower()
    if resp =='n':
        true = False

for i in range(len(lista)):
    if int(lista[int(i)])%2==0:
        par.append(lista[int(i)])
    else:
        impar.append(lista[int(i)])

print(f'lista {lista}\nimpar {impar}\npar{par}')





