
N = input()
X = list()

c = input()
X = c.split(' ')
menor = 1000
index = 0
for i in range(len(X)):
    k = X[i]
    if int(k) < menor:
        menor = int(X[i])
        index = i

print(f'Menor valor: {menor}')
print(f'Posiçao: {index}')
