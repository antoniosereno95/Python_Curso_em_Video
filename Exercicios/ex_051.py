termo1 = int(input('termo 1: '))
r = int(input('razao: '))
enesimo = termo1 + (10 - 1) * r #formula do enesimo termo de uma PA
for i in range(termo1,enesimo+r,r): #o +r é o enesimo mais a razao pq na vdd tem que ir ate o decimo primeiro numero da PA
    print(i)


