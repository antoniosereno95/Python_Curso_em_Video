import random
q = int(input('quantos jogos devo fazer? '))
for i in range(q):
    jogo = [0,0,0,0,0,0]
    for j in range(6):
            flag = True
            while flag ==True:
                r = random.randint(1, 61)
                for k in range(len(jogo)):
                    if int(r)==int(jogo[k]):
                        flag = True
                        pass
                    else:
                        flag = False
            jogo.append(r)
    jogo.sort()
    jogo1 = jogo[6:12]
    print(jogo1)
print('Esses sao seus jogos.\nBoa sorte!')
