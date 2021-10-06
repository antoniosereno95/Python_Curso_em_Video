#ex_086
m = [[],[],[]]
for j in range(3):
    for i in range(3):
        n = int(input(f'digite o valor para o bloco[{j},{i}]:'))
        m[j].append(n)
for l in range(3):
    print(m[l])

#ex_087
soma = soma3 = 0
for j in range(3):
    for i in range(3):
        if int(m[j][i])%2==0:
            soma += int(m[j][i])
print(f'letra a: {soma}')

for i in range(3):
    soma3 += m[i][2]
print(f'letra b: {soma3}')

maior = int(m[1][0])
for i in range(3):
    if int(m[1][i]) > maior:
         maior = int(m[1][i])
print(f'letra c: {maior}')
