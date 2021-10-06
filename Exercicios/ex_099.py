
def maior(* num):
    print('-='*23)
    print(f'analizando os valores passados...')
    maior = 0
    for i in num:
        print(f'{i} ', end='')
        if int(i) >= int(maior):
            maior = i
    print(f' Foram passados {len(num)} valores ao todo.')
    print(f'O mair valor encontrado foi {maior}.')
    print('-='*23)


#main
maior(9,9,8,7,5,2,0,1,4)





