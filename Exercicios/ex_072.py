
tupla = ('um','dois','tres','quatro','cinco')
n = int(input('digite um numero entra 1 e 5:'))
while n<1 or n>5:
    n = int(input('digite um numero entra 1 e 5:'))

print(f'o nuemro que voce digitou foi {tupla[n-1]}')




