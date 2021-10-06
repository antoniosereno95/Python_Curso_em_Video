sal = input('salario: ')
casa = input('valor da casa: ')
ano = input('em quantos anos voce vai pagar: ')

par = float(casa)/(int(ano)*12)
i30 = float(sal)*(30/100)

if float(par) > float(i30):
    print('emprestico negado')
else:
    print('emprestimo consedido')