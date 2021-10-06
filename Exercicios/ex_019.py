import random
l = input('nomes: ')
lista = l.split(' ')
k = int(len(lista))
n = random.randint(0,k)
print(lista)
print(lista[n])

random.shuffle(lista)
print(lista)