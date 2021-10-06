
atual = 2021
id = input('data de nascmento: ')

if int(atual) - int(id)==18:
    print('hora de se alistar')
elif int(atual) - int(id)<18:
    n = 18-(int(atual) - int(id))
    print('faltam ',n,' anos para voce se alistar ainda.')
elif int(atual) - int(id)>18:
    k = (int(atual) - int(id))-18
    print('voce esta atrasado ',k,' anos para se alistar')




