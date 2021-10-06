N = []
X = input()

for i in range(100):
    if i == 0:
        N.append(X)
    else:
        k = float(N[i-1])/2
        N.append(k)
print(N)
k = 0
for idx in range(100):
  print(f'N[{idx}] = {float(N[idx]):0.4f}')



